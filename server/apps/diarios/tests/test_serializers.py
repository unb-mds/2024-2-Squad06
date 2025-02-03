import pytest
from apps.diarios.serializers import FornecedorSerializer, ContratacaoSerializer, DiarioSerializer
from apps.diarios.models import Fornecedor, Contratacao, Diario
from datetime import date

@pytest.mark.django_db
def test_fornecedor_serializer_happy():
    fornecedor = Fornecedor.objects.create(nome="Fornecedor Teste", cnpj="00.000.000/0001-00")
    serializer = FornecedorSerializer(instance=fornecedor)
    data = serializer.data
    assert data["nome"] == "Fornecedor Teste"
    assert data["cnpj"] == "00.000.000/0001-00"

@pytest.mark.django_db
def test_contratacao_serializer_happy():
    fornecedor = Fornecedor.objects.create(nome="Fornecedor Teste", cnpj="00.000.000/0001-00")
    contratacao = Contratacao.objects.create(
        valor_mensal=100.00,
        valor_anual=1200.00,
        vigencia="2024",
        fornecedor=fornecedor
    )
    serializer = ContratacaoSerializer(instance=contratacao)
    data = serializer.data
    # Observe que os valores decimais podem ser serializados como strings.
    assert data["valor_mensal"] == "100.00"
    assert data["valor_anual"] == "1200.00"
    assert data["vigencia"] == "2024"
    assert data["fornecedor"]["nome"] == "Fornecedor Teste"

