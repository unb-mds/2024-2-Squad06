import requests
import re
import os
import json
from collections import defaultdict
from .models import Diario, Fornecedor
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Carrega os diários oficiais no banco de dados.'
    def handle(self, *args, **kwargs):
        try:
            carregar_diarios()
            self.stdout.write(self.style.SUCCESS('Diários carregados com sucesso.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao carregar diários: {e}'))

BASE_URL = "https://queridodiario.ok.org.br/api"
DOWNLOAD_DIR = "diarios_download"
caminho_completo = os.path.join(os.getcwd(), DOWNLOAD_DIR)

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def buscar_diarios_maceio(querystring, published_since, published_until):
    """Busca diários oficiais de Maceió por termos específicos e datas."""
    territory_id_maceio = "2704302"
    params = {
        "territory_ids": territory_id_maceio,
        "querystring": querystring,
        "published_since": published_since,
        "published_until": published_until,
        "page_size": 50
    }
    
    response = requests.get(f"{BASE_URL}/gazettes", params=params)
    if response.status_code == 200:
        return response.json().get("gazettes", [])
    else:
        raise Exception(f"Erro ao buscar diários: {response.status_code} {response.text}")

def baixar_arquivo(url, nome_arquivo):
    """Baixa um arquivo de diário."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        caminho_completo = os.path.join(DOWNLOAD_DIR, nome_arquivo)
        with open(caminho_completo, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return caminho_completo
    else:
        raise Exception(f"Erro ao baixar arquivo: {response.status_code} {response.text}")

def extrair_valores(texto):
    """Extrai valores monetários de um texto."""
    padrao_valores = r"R\$ ?\d{1,3}(?:\.\d{3})*,\d{2}"
    return re.findall(padrao_valores, texto)

def converter_para_float(valor_str):
    """Converte valores monetários de string para float."""
    valor_str = valor_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
    return float(valor_str)

def salvar_resultados(resultados, nome_arquivo="resultados.json"):
    """Salva os resultados processados em um arquivo JSON."""
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)

def extrair_fornecedores(texto):
    """Extrai fornecedores das licitações a partir do texto."""
    padrao_fornecedores = re.compile(r'(?:Fornecedor|Empresa|Contratado):?\s*([^\n]+)', re.IGNORECASE)
    padrao_cnpj = re.compile(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b', re.IGNORECASE)

    fornecedores = defaultdict(lambda: {'nome': '', 'cnpj': '', 'ocorrencias': 0})
    linhas = texto.split('\n')

    for i, linha in enumerate(linhas):
        match_fornecedor = padrao_fornecedores.search(linha)
        if match_fornecedor:
            nome = match_fornecedor.group(1).strip()
            # Procurar o CNPJ nas próximas linhas
            cnpj = None
            for j in range(i+1, min(i+5, len(linhas))):
                match_cnpj = padrao_cnpj.search(linhas[j])
                if match_cnpj:
                    cnpj = match_cnpj.group(0).strip()
                    break
            if not cnpj:
                cnpj = "/"
            fornecedores[cnpj]['nome'] = nome
            fornecedores[cnpj]['cnpj'] = cnpj
            fornecedores[cnpj]['ocorrencias'] += 1
    
    return fornecedores

def processar_diarios(diarios):
    """Baixa e processa diários, extraindo valores monetários e fornecedores."""
    resultados = []
    
    for diario in diarios:
        try:
            caminho = baixar_arquivo(diario.get("txt_url"), f"{diario['date']}.txt")
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()
                valores = extrair_valores(conteudo)
                fornecedores = extrair_fornecedores(conteudo)
                
            valor_final = sum(converter_para_float(v) for v in valores)
            
            diario_obj = Diario.objects.create(
                date=diario["date"],
                url=diario["url"],
                excerpts=diario.get("excerpts", ""),
                edition=diario["edition"],
                is_extra_edition=diario.get("is_extra_edition", False),
                txt_url=diario["txt_url"],
                valor_final=valor_final
            )
            
            for cnpj, dados in fornecedores.items():
                Fornecedor.objects.create(
                    nome=dados['nome'],
                    cnpj=dados['cnpj'],
                    ocorrencias=dados['ocorrencias'],
                    diario=diario_obj
                )
            
            resultados.append({
                "date": diario["date"],
                "url": diario["url"],
                "excerpts": diario.get("excerpts"),
                "edition": diario["edition"],
                "is_extra_edition": diario.get("is_extra_edition"),
                "txt_url": diario["txt_url"],
                "valor_final": valor_final,
                "fornecedores": list(fornecedores.values()),
            })
        except Exception as e:
            print(f"Erro ao processar diário: {e}")
    limpar_pasta(caminho_completo)
    return resultados

def limpar_pasta(pasta):
    """Remove todos os arquivos dentro da pasta especificada."""
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        try:
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
        except Exception as e:
            print(f"Erro ao apagar arquivo {caminho_arquivo}: {e}")
            
from .models import Diario

from .models import Diario, Fornecedor

def salvar_resultados_no_banco(resultados):
    diarios_a_inserir = []
    fornecedores_a_inserir = []
    
    for resultado in resultados:
        # Verifica se o diário já existe no banco de dados com base no campo txt_url
        if not Diario.objects.filter(txt_url=resultado["txt_url"]).exists():
            diario_obj = Diario(
                date=resultado["date"],
                url=resultado["url"],
                excerpts=resultado.get("excerpts"),
                edition=resultado["edition"],
                txt_url=resultado["txt_url"],
                valor_final=resultado["valor_final"],
                is_extra_edition=resultado.get("is_extra_edition", False),
            )
            diarios_a_inserir.append(diario_obj)
            
            # Adiciona os fornecedores associados ao diário
            for fornecedor in resultado["fornecedores"]:
                fornecedores_a_inserir.append(Fornecedor(
                    nome=fornecedor["nome"],
                    cnpj=fornecedor["cnpj"],
                    ocorrencias=fornecedor["ocorrencias"],
                    diario=diario_obj
                ))
    
    # Insere todos os registros de uma vez
    if diarios_a_inserir:
        Diario.objects.bulk_create(diarios_a_inserir)
        Fornecedor.objects.bulk_create(fornecedores_a_inserir)
    
    # Insere todos os registros de uma vez
    if diarios_a_inserir:
        Diario.objects.bulk_create(diarios_a_inserir)
        
def get_dados_salvos():
    return list(Diario.objects.values(
        "date", "url","excerpts", "edition", "is_extra_edition", "txt_url", "valor_final"
    ))

