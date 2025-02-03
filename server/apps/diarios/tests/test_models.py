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
