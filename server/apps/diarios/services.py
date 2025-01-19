import os
import re
import json
import requests
from .models import Diario, Fornecedor, Contratacao
import logging

# Configurando o logger para identificar erros
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class Controladores:
    def __init__(self):
        self._url_base = "https://queridodiario.ok.org.br/api"
        self._diretorio_download = "diarios_download"
        self._caminho_completo = os.path.join(os.getcwd(), self._diretorio_download)
        os.makedirs(self._diretorio_download, exist_ok=True)

    def buscar_diarios_maceio(self, termo_busca, data_inicio, data_fim):
        id_territorio_maceio = "2704302"
        params = {
            "territory_ids": id_territorio_maceio,
            "querystring": termo_busca,
            "published_since": data_inicio,
            "published_until": data_fim,
            "page_size": 50
        }
        
        response = requests.get(f"{self._url_base}/gazettes", params=params)
        if response.status_code == 200:
            return response.json().get("gazettes", [])
        else:
            raise Exception(f"Erro ao buscar diários: {response.status_code} {response.text}")

    def baixar_diario(self, url, nome_arquivo):
        resposta = requests.get(url, stream=True)
        if resposta.status_code == 200:
            caminho_arquivo = os.path.join(self._caminho_completo, nome_arquivo)
            with open(caminho_arquivo, "wb") as arquivo:
                for parte in resposta.iter_content(chunk_size=8192):
                    arquivo.write(parte)
            return caminho_arquivo
        raise Exception(f"Erro ao baixar arquivo: {resposta.status_code} {resposta.text}")

    def converter_valor(self, texto):
        try:
            valor_limpo = re.sub(r'[^0-9,]', '', texto)
            if not valor_limpo:
                return None
            valor_limpo = valor_limpo.replace(",", ".").strip()
            if re.match(r'^\d+(\.\d+)?$', valor_limpo):
                return float(valor_limpo)
            else:
                logger.warning(f"Formato de valor inesperado: {texto}")
                return None
        except Exception as e:
            logger.warning(f"Erro ao converter valor: {texto}. Erro: {e}")
            return None

    def extrair_valores_detalhados(self, texto):
        padrao_valor = re.compile(
            r"[Vv]alor\s*(mensal|total|anual)?[^\d]*(?:de|:)?\s*(R\$)?\s?(\d{1,3}(?:\.\d{3})*,\d{2})", 
            re.IGNORECASE
        )
        valores = {"mensal": None, "total": None}

        for match in padrao_valor.finditer(texto):
            tipo = match.group(1).lower() if match.group(1) else None
            valor = self.converter_valor(match.group(3))
            if tipo == "mensal":
                valores["mensal"] = valor
            elif tipo in ["total", "anual"]:
                valores["total"] = valor

        return valores
        
    def extrair_nomes_empresas(self, texto):
        padrao_nome = re.compile(r'(?:Fornecedor|Empresa|Contratado):?\s*([^\n]+)', re.IGNORECASE)
        return [match.group(1).strip() for match in padrao_nome.finditer(texto)]
    
    def extrair_cnpjs(self, texto):
        padrao_cnpj = re.compile(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b')
        return [match.group(0) for match in padrao_cnpj.finditer(texto)]
    
    def extrair_vigencia_contrato(self, texto):
        padrao_vigencia = re.compile(
            r'(vigência.*?(?:\d{1,2}/\d{1,2}/\d{4}|\d{1,2}-\d{1,2}-\d{4})|prazo contratual.*?\d+\s*(meses|anos))',
            re.IGNORECASE,
        )
        return [match.group(0) for match in padrao_vigencia.finditer(texto)]

    def criar_fornecedores_contratacao(self, diario, publicacao):
        valores_detalhados = self.extrair_valores_detalhados(publicacao)
        fornecedores = self.extrair_fornecedores(publicacao)
        vigencia = self.extrair_vigencia_contrato(publicacao)

        for fornecedor_data in fornecedores:
            fornecedor_obj, created = Fornecedor.objects.get_or_create(
                nome=fornecedor_data["nome"], 
                cnpj=fornecedor_data["cnpj"]
            )
            fornecedor_obj.save()

            contratacao = Contratacao.objects.create(
                valor_mensal=valores_detalhados.get("mensal"),
                valor_total=valores_detalhados.get("total"),
                vigencia=vigencia[0] if vigencia else None,
            )

            diario.contratacoes.add(contratacao)
            diario.fornecedores.add(fornecedor_obj)

        diario.save()
   
    def extrair_fornecedores(self, texto):
        nomes = self.extrair_nomes_empresas(texto)
        cnpjs = self.extrair_cnpjs(texto)

        fornecedores = []
        for i in range(max(len(nomes), len(cnpjs))):
            nome = nomes[i] if i < len(nomes) else "Nome desconhecido"
            cnpj = cnpjs[i] if i < len(cnpjs) else "CNPJ desconhecido"
            fornecedores.append({"nome": nome, "cnpj": cnpj})
        
        return fornecedores
    
    def ler_arquivo(self, caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
        
    def separar_publicacoes(self, texto):
        padrao = re.compile(r'(PORTARIA|RESOLVE|CONTRATAÇÃO|OBJETO|CONSELHO|PROCURADORIA|AGÊNCIA)\s*[^\n]+', re.IGNORECASE)
        publicacoes = padrao.split(texto)
        return [pub.strip() for pub in publicacoes if pub.strip()]

    def filtrar_publicacoes_validas(self, publicacoes):
        palavras_chave_contratacao = re.compile(
            r'(contrato|fornecedor|valor total|valor mensal|contratação)', re.IGNORECASE
        )
        return [
            pub for pub in publicacoes 
            if palavras_chave_contratacao.search(pub) and self.extrair_valores_detalhados(pub)["mensal"] is not None
        ]

    def processar_diarios(self, diarios):
        resultados = []

        for diario in diarios:
            try:
                caminho = self.baixar_diario(diario["txt_url"], f"{diario['date']}.txt")
                conteudo = self.ler_arquivo(caminho)

                publicacoes = self.separar_publicacoes(conteudo)
                publicacoes_validas = self.filtrar_publicacoes_validas(publicacoes)

                diario_obj = Diario(
                    date=diario["date"],
                    url=diario["url"],
                    edition=diario["edition"],
                    is_extra_edition=diario.get("is_extra_edition", False),
                    txt_url=diario["txt_url"],
                )

                for publicacao in publicacoes_validas:
                    self.criar_fornecedores_contratacao(diario_obj, publicacao)

                diario_obj.save()

                resultados.append({
                    "diario_obj": diario_obj,
                    "publicacoes_processadas": len(publicacoes_validas),
                })

            except Exception as erro:
                logger.error(f"Erro ao processar diário {diario['txt_url']}: {erro}")
                raise Exception(f"Erro ao processar diário {diario['txt_url']}: {erro}")

        return resultados

    def limpar_diretorio(self):
        for arquivo in os.listdir(self._caminho_completo):
            caminho_arquivo = os.path.join(self._caminho_completo, arquivo)
            try:
                if os.path.isfile(caminho_arquivo):
                    os.remove(caminho_arquivo)
            except Exception as erro:
                print(f"Erro ao apagar arquivo {caminho_arquivo}: {erro}")

    def salvar_resultados(self, resultados):
        caminho_arquivo = os.path.join(self._caminho_completo, "resultados.json")
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(resultados, arquivo, ensure_ascii=False, indent=4)

    def salvar_banco_dados(self, diarios):
        resultados = self.processar_diarios(diarios)
        try:
            for resultado in resultados:
                diario_obj = Diario.objects.get(id=resultado["diario_id"])
                diario_obj.save()

            logger.info(f"Resultados salvos no banco de dados com sucesso: {len(resultados)} diários processados.")
            return resultados

        except Exception as erro:
            logger.error(f"Erro ao salvar resultados no banco de dados: {erro}")
            raise Exception(f"Erro ao salvar resultados no banco de dados: {erro}")
