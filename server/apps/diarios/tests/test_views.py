import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.diarios.models import Diario, Fornecedor, Contratacao
from datetime import date, timedelta

@pytest.fixture
def api_client():
    return APIClient()

# Para testar a view que busca diários (BuscarDiariosAPIView incompleta)
@pytest.mark.django_db
def test_buscar_diarios_api_happy(api_client, monkeypatch):
    url = reverse("buscar_diarios")
    
    # Monkeypatch: simula a função buscar_diarios_maceio para retornar um diário fake
    def fake_buscar_diarios_maceio(query, published_since, published_until):
        return [{
            "date": "2024-01-01",
            "url": "http://example.com",
            "txt_url": "http://example.com/diario.txt",
            "edicao": "Extraordinária",
            "edicao_extra": True,
            "resumo": "Teste"
        }]
    monkeypatch.setattr("apps.diarios.services.Controladores.buscar_diarios_maceio", fake_buscar_diarios_maceio)
    
    # Monkeypatch: simula processar_diarios para retornar um resultado fixo
    def fake_processar_diarios(self,diarios):
        return [{
            "date": "2024-01-01",
            "url": "http://example.com",
            "txt_url": "http://example.com/diario.txt",
            "excerpts": "Teste",
            "contratacoes": []
        }]
    monkeypatch.setattr("apps.diarios.services.Controladores.processar_diarios", fake_processar_diarios)
    
    # Teste passando parâmetros válidos
    response = api_client.get(url, {
        "query": "teste",
        "data_inicial": "2024-01-01",
        "data_final": "2024-01-16"
    })
    assert response.status_code == 200
    data = response.json()
    assert "diarios" in data
    assert data["diarios"][0]["date"] == "2024-01-01"

@pytest.mark.django_db
def test_buscar_diarios_api_bad_date(api_client):
    url = reverse("buscar_diarios")
    response = api_client.get(url, {"data_inicial": "data_invalida"})
    assert response.status_code == 400

# Para a view GetGazettesAPIView (ListAPIView)
@pytest.mark.django_db
def test_get_gazettes_api(api_client):
    url = reverse("getGazettes")
    response = api_client.get(url)
    assert response.status_code == 200
