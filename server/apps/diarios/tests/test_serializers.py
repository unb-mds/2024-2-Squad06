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

@pytest.mark.django_db
def test_diario_serializer_happy():
    fornecedor = Fornecedor.objects.create(nome="Fornecedor Teste", cnpj="00.000.000/0001-00")
    contratacao = Contratacao.objects.create(
        valor_mensal=200.00,
        valor_anual=2400.00,
        vigencia="2025",
        fornecedor=fornecedor
    )
    diario = Diario.objects.create(
        date=date(2025, 2, 4),
        url="https://example.com/diario",
        excerpts="Conteúdo do diário",
        txt_url="https://example.com/diario.txt",
    )
    diario.contratacao.add(contratacao)  # Adiciona a relação ManyToMany
    serializer = DiarioSerializer(instance=diario)
    data = serializer.data
    
    assert data["date"] == "2025-02-04"
    assert data["url"] == "https://example.com/diario"
    assert data["excerpts"] == "Conteúdo do diário"
    assert data["txt_url"] == "https://example.com/diario.txt"
    assert len(data["contratacao"]) == 1
    assert data["contratacao"][0]["valor_mensal"] == "200.00"
    assert data["contratacao"][0]["valor_anual"] == "2400.00"
    assert data["contratacao"][0]["vigencia"] == "2025"
    assert data["contratacao"][0]["fornecedor"]["nome"] == "Fornecedor Teste"
