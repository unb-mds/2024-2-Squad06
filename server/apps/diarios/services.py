import os
import requests
import logging
from datetime import datetime, timedelta
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


# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://queridodiario.ok.org.br/api"
DOWNLOAD_DIR = "diarios_download"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Função para buscar diários

def buscar_diarios(territory_id, querystring, published_since, published_until):
    """Busca diários oficiais por termos específicos e datas."""
    params = {
        "territory_ids": territory_id,
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

# Função para processar diários

def processar_diarios(diarios):
    """Processa diários baixando e extraindo informações."""
    resultados = []

    for diario in diarios:
        try:
            # Baixa o arquivo do diário
            response = requests.get(diario.get("txt_url"), stream=True)
            if response.status_code == 200:
                caminho_arquivo = os.path.join(DOWNLOAD_DIR, f"{diario['date']}.txt")
                with open(caminho_arquivo, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                # Processa o conteúdo do diário
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                # Exemplo: Extração de dados (personalize conforme necessário)
                valor_final = 0  # Substituir com cálculo real
                fornecedores = []  # Substituir com extração real

                # Monta o resultado para salvar no banco
                resultados.append({
                    "date": diario["date"],
                    "url": diario["url"],
                    "excerpts": diario.get("excerpts", ""),
                    "edition": diario["edition"],
                    "txt_url": diario["txt_url"],
                    "valor_final": valor_final,
                    "fornecedores": fornecedores
                })
            else:
                raise Exception(f"Erro ao baixar arquivo: {response.status_code} {response.text}")
        except Exception as e:
            logger.error(f"Erro ao processar diário {diario['date']}: {e}")

    return resultados

# Função para salvar resultados no banco

def salvar_resultados_no_banco(resultados):
    """Salva os resultados processados no banco de dados."""
    diarios_a_inserir = []
    fornecedores_a_inserir = []

    for resultado in resultados:
        # Verifica se o diário já existe no banco
        if not Diario.objects.filter(txt_url=resultado["txt_url"]).exists():
            diario_obj = Diario(
                date=resultado["date"],
                url=resultado["url"],
                excerpts=resultado.get("excerpts", ""),
                edition=resultado["edition"],
                txt_url=resultado["txt_url"],
                valor_final=resultado["valor_final"]
            )
            diarios_a_inserir.append(diario_obj)

            # Adiciona fornecedores
            for fornecedor in resultado["fornecedores"]:
                fornecedores_a_inserir.append(Fornecedor(
                    nome=fornecedor["nome"],
                    cnpj=fornecedor["cnpj"],
                    ocorrencias=fornecedor["ocorrencias"],
                    diario=diario_obj
                ))

    # Inserção em lote no banco
    if diarios_a_inserir:
        Diario.objects.bulk_create(diarios_a_inserir)
        Fornecedor.objects.bulk_create(fornecedores_a_inserir)

# Função principal de carregamento

def carregar_diarios():
    """Função principal para buscar, processar e salvar diários."""
    try:
        logger.info("Iniciando carregamento de diários...")
        hoje = datetime.now().date()
        sete_dias_atras = hoje - timedelta(days=7)

        diarios = buscar_diarios(
            territory_id="2704302",
            querystring="contrato",
            published_since=sete_dias_atras.strftime("%Y-%m-%d"),
            published_until=hoje.strftime("%Y-%m-%d")
        )

        resultados = processar_diarios(diarios)
        salvar_resultados_no_banco(resultados)

        logger.info(f"Carregamento concluído. {len(resultados)} diários processados e salvos.")
    except Exception as e:
        logger.error(f"Erro no carregamento: {e}")

