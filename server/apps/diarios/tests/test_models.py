import pytest
from apps.diarios.models import Fornecedor, Contratacao, Diario
from datetime import date

@pytest.mark.django_db
def test_fornecedor_str_happy():
    fornecedor = Fornecedor.objects.create(nome="Fornecedor Teste", cnpj="00.000.000/0001-00")
    assert str(fornecedor) == "Fornecedor Teste"

@pytest.mark.django_db
def test_contratacao_str_happy():
    fornecedor = Fornecedor.objects.create(nome="Fornecedor Teste", cnpj="00.000.000/0001-00")
    contratacao = Contratacao.objects.create(
        valor_mensal=100.00,
        valor_anual=1200.00,
        vigencia="2024",
        fornecedor=fornecedor
    )
    esperado = f"Contratação de {fornecedor.nome} (Vigência: 2024)"
    assert str(contratacao) == esperado

@pytest.mark.django_db
def test_get_valores_salvos_vazio():
    # Se não houver nenhum objeto Diario, a lista retornada deve ser vazia.
    resultados = Diario.get_valores_salvos()
    assert resultados == []

@pytest.mark.django_db
def test_get_valores_salvos_com_dados():
    fornecedor = Fornecedor.objects.create(nome="Fornecedor Teste", cnpj="00.000.000/0001-00")
    contratacao = Contratacao.objects.create(
        valor_mensal=200.00,
        valor_anual=2400.00,
        vigencia="2025",
        fornecedor=fornecedor
    )
    diario = Diario.objects.create(
        date=date(2025, 1, 1),
        url="https://example.com",
        excerpts="Trecho de exemplo",
        txt_url="https://example.com/text.txt",
        contratacao=contratacao
    )
    resultados = Diario.get_valores_salvos()
    assert len(resultados) == 1
    assert resultados[0]["date"] == diario.date
    assert resultados[0]["url"] == diario.url
    assert resultados[0]["excerpts"] == diario.excerpts
    assert resultados[0]["txt_url"] == diario.txt_url
    assert resultados[0]["contratacao"] == list(contratacao)
