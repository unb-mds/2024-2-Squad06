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
        for match in re.finditer(r"(Vig[ê|e]ncia|Per[í|i]odo):?\s*(.*)\n", texto):
            contratos.append(match.group(2).strip())
        return contratos

    @staticmethod
    def extrair_fornecedores(texto):
        padrao_fornecedor = re.compile(r'(?:Fornecedor|Empresa|Contratado):?\s*([^\n]+)', re.IGNORECASE)
        padrao_cnpj = re.compile(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b', re.IGNORECASE)
        fornecedores = defaultdict(lambda: {'nome': '', 'cnpj': ''})
        linhas = texto.split('\n')
        for i, linha in enumerate(linhas):
            match_fornecedor = padrao_fornecedor.search(linha)
            if match_fornecedor:
                nome = match_fornecedor.group(1).strip()
                cnpj = None
                for j in range(i + 1, min(i + 5, len(linhas))):
                    match_cnpj = padrao_cnpj.search(linhas[j])
                    if match_cnpj:
                        cnpj = match_cnpj.group(0).strip()
                        break
                cnpj = cnpj or "/"
                fornecedores[cnpj]['nome'] = nome
                fornecedores[cnpj]['cnpj'] = cnpj
        return fornecedores

    @staticmethod
    def converter_para_float(valor):
        return float(valor.replace("R$", "").replace(".", "").replace(",", ".").strip())
    
    def extrair_valores(self, texto):
        padrao_valores = r"R\$ ?\d{1,3}(?:\.\d{3})*,\d{2}"
        return re.findall(padrao_valores, texto)

    def processar_diarios(self, diarios):
        resultados = []
        for diario in diarios:
            try:
                caminho_arquivo = self.baixar_arquivo(diario["txt_url"], f"{diario['date']}.txt")
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    valores = self.extrair_valores(conteudo)
                    fornecedores = self.extrair_fornecedores(conteudo)
                    contratos = self.extrair_info_contratos(conteudo)
                    diario_obj = Diario(
                        date=diario["date"],
                        url=diario["url"],
                        excerpts=diario.get("excerpts", ""),
                        txt_url=diario["txt_url"],
                    )
                    resultado = {
                        "date": diario["date"],
                        "url": diario["url"],
                        "txt_url": diario["txt_url"],
                        "fornecedores": list(fornecedores.values()),
                        "contratos": contratos
                    }
                    resultados.append(resultado)
            except Exception as e:
                print(f"Erro ao processar diário {diario['date']}: {e}")
        self.limpar_diretorio(DIRETORIO_DOWNLOAD)
        return resultados

    @staticmethod
    def limpar_diretorio(diretorio):
        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)

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
