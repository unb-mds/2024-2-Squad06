import os
import re
import requests
from collections import defaultdict
from .models import Diario, Fornecedor, Contratacao

URL_BASE = "https://queridodiario.ok.org.br/api"
DIRETORIO_DOWNLOAD = "diarios_download"
os.makedirs(DIRETORIO_DOWNLOAD, exist_ok=True)

class Controladores:
    def __init__(self):
        self.diarios = []

    @staticmethod
    def buscar_diarios_maceio(querystring, published_since, published_until):
        territory_id_maceio = "2704302"
        params = {
            "territory_ids": territory_id_maceio,
            "querystring": querystring,
            "published_since": published_since,
            "published_until": published_until,
            "page_size": 50
        }
        response = requests.get(f"{URL_BASE}/gazettes", params=params)
        if response.status_code == 200:
            return response.json().get("gazettes", [])
        else:
            raise Exception(f"Erro ao buscar diários: {response.status_code} {response.text}")

    @staticmethod
    def baixar_arquivo(url, nome_arquivo):
        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()
        caminho_arquivo = os.path.join(DIRETORIO_DOWNLOAD, nome_arquivo)
        with open(caminho_arquivo, "wb") as arquivo:
            for chunk in resposta.iter_content(chunk_size=8192):
                arquivo.write(chunk)
        return caminho_arquivo

    def associar_valores_a_contratos(texto):
        padrao_valores = r"R\$ ?\d{1,3}(?:\.\d{3})*,\d{2}"
        valores = re.findall(padrao_valores, texto)
        contratos = ["Contrato 1", "Contrato 2", "Contrato 3"]
        fornecedores = ["Fornecedor A", "Fornecedor B", "Fornecedor C", "Fornecedor D"]
        associacoes = []
        contrato_idx = 0
        fornecedor_idx = 0
        for i in range(0, len(valores), 2):
            if contrato_idx >= len(contratos):
                break
            contrato = contratos[contrato_idx] if contrato_idx < len(contratos) else None
            fornecedor = fornecedores[fornecedor_idx]
            associacoes.append({
                "contrato": contrato,
                "fornecedor": fornecedor,
                "valores": valores[i:i + 2]
            })
            fornecedor_idx += 1
            if fornecedor_idx >= len(fornecedores):
                break
            if fornecedor_idx % len(fornecedores) == 0:
                contrato_idx += 1
        return associacoes

    def converter_valor(self, valor):
        valor = valor.replace('.', '').replace(',', '.')
        return float(valor)

    @staticmethod
    def extrair_info_contratos(texto):
        contratos = []
        padrao_vigencia = re.compile(r"VIG[Ê|E]NCIA\s+(?:DE\s+|DA\s+ARP)?:?\s*(\d+)", re.IGNORECASE)
        match = padrao_vigencia.search(texto)
        if match:
            vigencia = match.group(1).strip()
            contratos.append(f"{vigencia} meses")
        return contratos

    @staticmethod
    def extrair_fornecedores(texto):
        padrao_fornecedor = re.compile(r'(?:fornecedor registrado: empresa|fornecedor registrado|Fornecedor|Empresa|Contratado):?\s*([^\n\r]+(?:[^\n\r]*))', re.IGNORECASE| re.DOTALL)
        padrao_cnpj = re.compile(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b', re.IGNORECASE)
        padrao_data = re.compile(r'(\d{1,2})\s*de\s*(\w+)\s*de\s*(\d{4})', re.IGNORECASE)

        palavras_ignoradas = ["especializada", "foram previamente escolhido","(es) foram","é equivalente"]

        fornecedores = defaultdict(lambda: {'nome': '', 'cnpj': '','data de assinatura': ''})
        linhas = texto.split('\n')

        for i, linha in enumerate(linhas):
            match_fornecedor = padrao_fornecedor.search(linha)
            if match_fornecedor:
                nome = match_fornecedor.group(1).strip()

                while i + 1 < len(linhas) and not padrao_cnpj.search(linhas[i + 1]):
                    if not nome.endswith(" "):
                        nome += " "

                    nome += linhas[i + 1].strip()
                    i += 1

                nome = re.split('[,.:;]', nome)[0].strip()

                if any(palavra.lower() in nome.lower() for palavra in palavras_ignoradas):
                    continue
                
                cnpj = None
                data_assinatura = None
                for j in range(i + 1, len(linhas)):
                    match_cnpj = padrao_cnpj.search(linhas[j])
                    if match_cnpj:
                        cnpj = match_cnpj.group(0).strip()
                    match_data = padrao_data.search(linhas[j])
                    if match_data:
                        dia = match_data.group(1)
                        mes = match_data.group(2).lower() 
                        ano = match_data.group(3)
                        data_assinatura = f"{dia} de {mes} de {ano}"
                        break
                    
                cnpj = cnpj or "/"
                data_assinatura = data_assinatura or "/"
                fornecedores[cnpj]['nome'] = nome
                fornecedores[cnpj]['cnpj'] = cnpj
                fornecedores[cnpj]['data_assinatura'] = data_assinatura

        return fornecedores

    @staticmethod
    def converter_para_float(valor):
        return float(valor.replace("R$", "").replace(".", "").replace(",", ".").strip())
    
    def extrair_valores(self, texto):
        padrao_valores = r"R\$ ?\d{1,3}(?:\.\d{3})*,\d{2}"
        return re.findall(padrao_valores, texto)
    
    @staticmethod
    def filtrar_publicacoes(texto):
        blocos_contratos = []
        padrao_secao = r"(AGÊNCIA DE LICITAÇÕES|SECRETARIA MUNICIPAL [^\n]+|CONTRATO|CONTRATAÇÃO|INSTITUTO DE [^\n]+|FUNDAÇÃO [^\n]+|PROCURADORIA [^\n]+)"
        secoes = re.split(padrao_secao, texto, flags=re.IGNORECASE)

        bloco_atual = []
        palavras_proibidas = r"(inexigibilidade|processo administrativo)"

        for i in range(len(secoes) - 1):
            if re.search(r"(CONTRATO|CONTRATAÇÃO)", secoes[i], flags=re.IGNORECASE):
                if bloco_atual:
                    bloco_completo = "".join(bloco_atual)
                    if not re.search(palavras_proibidas, bloco_completo, flags=re.IGNORECASE):
                        blocos_contratos.append(bloco_completo)
                bloco_atual = [secoes[i], secoes[i + 1]]
            elif re.search(r"(INSTITUTO DE|FUNDAÇÃO|PROCURADORIA)", secoes[i], flags=re.IGNORECASE):
                if bloco_atual:
                    bloco_completo = "".join(bloco_atual)
                    if not re.search(palavras_proibidas, bloco_completo, flags=re.IGNORECASE):
                        blocos_contratos.append(bloco_completo)
                bloco_atual = []
            else:
                bloco_atual.append(secoes[i] + secoes[i + 1])
                
        if bloco_atual:
            bloco_completo = "".join(bloco_atual)
            if not re.search(palavras_proibidas, bloco_completo, flags=re.IGNORECASE):
                blocos_contratos.append(bloco_completo)

        return blocos_contratos



    def processar_diarios(self, diarios):
        resultados = []
        for diario in diarios:
            try:
                caminho_arquivo = self.baixar_arquivo(diario["txt_url"], f"{diario['date']}.txt")
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    blocos_contratos = self.filtrar_publicacoes(conteudo)
                    contratacoes = []
                    if blocos_contratos:
                        for bloco in blocos_contratos:
                            valores = self.extrair_valores(bloco)  
                            fornecedores = self.extrair_fornecedores(bloco)  
                            contratos = self.extrair_info_contratos(bloco)  
                            vigencia = contratos[0] if contratos else None  
                            if valores:
                                mensal = self.converter_para_float(valores[0]) if len(valores) >= 1 else None
                                anual = self.converter_para_float(valores[1]) if len(valores) >= 2 else None

                                if vigencia:  
                                    anual *= 12
                                    anual = round(anual, 2)

                                for fornecedor_data in fornecedores.values():
                                    contratacao = {
                                        "fornecedor": {
                                            "nome": fornecedor_data['nome'],
                                            "cnpj": fornecedor_data['cnpj'],
                                            "data de assinatura":fornecedor_data["data_assinatura"]
                                        },
                                        "valores": {
                                            "mensal": mensal,
                                            "anual": anual
                                        },
                                        "vigencia": contratos[0] if contratos else None
                                    }
                                    contratacoes.append(contratacao)
                    resultados.append({
                        "date": diario["date"],
                        "url": diario["url"],
                        "txt_url": diario["txt_url"],
                        "excerpts": diario.get("excerpts", ""),
                        "contratacoes": contratacoes
                    })
            except Exception as e:
                print(f"Erro ao processar diário {diario['date']}: {e}")
        self.limpar_diretorio(DIRETORIO_DOWNLOAD)
        return resultados

    @staticmethod
    def limpar_diretorio(diretorio):
        try:
            for arquivo in os.listdir(diretorio):
                caminho_arquivo = os.path.join(diretorio, arquivo)
                if os.path.isfile(caminho_arquivo):
                    os.remove(caminho_arquivo)
        except Exception as e:
            print(f"Erro ao limpar diretório {diretorio}: {e}")

    def salvar_no_banco_de_dados(self, resultados):
        diarios_para_criar = []
        fornecedores_para_criar = []
        contratos_para_criar = []
        for resultado in resultados:
            if not Diario.objects.filter(txt_url=resultado["txt_url"]).exists():
                diario_obj = Diario(
                    date=resultado["date"],
                    url=resultado["url"],
                    excerpts=resultado.get("excerpts"),
                    txt_url=resultado["txt_url"],
                    valor_final=resultado["valor_final"],
                )
                diarios_para_criar.append(diario_obj)
                for fornecedor in resultado["fornecedores"]:
                    fornecedores_para_criar.append(Fornecedor(
                        nome=fornecedor["nome"],
                        cnpj=fornecedor["cnpj"],
                        diario=diario_obj
                    ))
        Diario.objects.bulk_create(diarios_para_criar)
        Fornecedor.objects.bulk_create(fornecedores_para_criar)
        Contratacao.objects.bulk_create(contratos_para_criar)

    def obter_dados_salvos(self):
        return list(Diario.objects.values(
            "date", "url", "txt_url", "valor_final"
        ))
