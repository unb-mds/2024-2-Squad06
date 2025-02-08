import unittest
import json
from unittest.mock import patch, MagicMock
from datetime import datetime
from rest_framework.test import APIRequestFactory
from rest_framework import status
from apps.diarios.views import (
    RequisicaoAPIView,
    DiariosView,
    FornecedoresListAPIView,
    FornecedorByNameAPIView,
    DiariosPorFornecedorByIdAPIView,
)

class TestViewsWithoutDatabase(unittest.TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    @patch("apps.diarios.views.Controladores")
    def test_requisicao_api_view(self, mock_controladores):
        mock_controlador = mock_controladores.return_value
        mock_controlador.buscar_diarios_maceio.return_value = [
            {"date": "2024-01-01", "url": "http://example.com", "excerpts": "Teste"}
        ]
        mock_controlador.processar_diarios.return_value = [
            {"date": "2024-01-01", "url": "http://example.com", "excerpts": "Teste"}
        ]
        request = self.factory.get(
            "/requisicao/",
            {
                "query": "contratação",
                "data_inicial": "2024-01-01",
                "data_final": "2024-01-15"
            }
        )
        view = RequisicaoAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "diarios": [{"date": "2024-01-01", "url": "http://example.com", "excerpts": "Teste"}]
        })

    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_view(self, mock_diario_objects):
        mock_diario = MagicMock()
        mock_diario.id = 1
        mock_diario.date = datetime(2024, 1, 1).date()
        mock_diario.url = "http://example.com"
        mock_diario.txt_url = "http://example.com/txt"
        mock_diario.excerpts = "Conteúdo do diário"
        mock_diario.contratacoes.all.return_value = []
        mock_qs = [mock_diario]
        mock_diario_objects.all.return_value.filter.return_value.distinct.return_value.order_by.return_value = mock_qs
        request = self.factory.get("/diarios/", {"data_publicacao": "2024-01-01"})
        view = DiariosView.as_view()
        response = view(request)
        data = json.loads(response.content.decode("utf-8"))
        expected = [{
            "id": 1,
            "data_publicacao": "2024-01-01",
            "url": "http://example.com",
            "txt_url": "http://example.com/txt",
            "excerpts": "Conteúdo do diário",
            "contratacoes": []
        }]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected)

    @patch("apps.diarios.views.Fornecedor.objects")
    def test_fornecedores_list_api_view(self, mock_fornecedor_objects):
        mock_fornecedor = MagicMock()
        mock_fornecedor.id = 1
        mock_fornecedor.nome = "Fornecedor Teste"
        mock_fornecedor.cnpj = "00.000.000/0001-00"
        mock_qs = [mock_fornecedor]
        mock_fornecedor_objects.annotate.return_value.filter.return_value.order_by.return_value = mock_qs
        request = self.factory.get("/fornecedores/")
        view = FornecedoresListAPIView.as_view()
        response = view(request)
        result = [dict(item) for item in response.data]
        expected = [{
            "nome": "Fornecedor Teste",
            "cnpj": "00.000.000/0001-00",
            "contract_count": 1
        }]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, expected)

    @patch("apps.diarios.views.Fornecedor.objects")
    def test_fornecedor_by_name_api_view(self, mock_fornecedor_objects):
        mock_fornecedor = MagicMock()
        mock_fornecedor.id = 1
        mock_fornecedor_objects.get.return_value = mock_fornecedor
        request = self.factory.post("/fornecedor/", {"nome": "Fornecedor Teste"}, format="json")
        view = FornecedorByNameAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"id": 1})

    @patch("apps.diarios.views.Fornecedor.objects")
    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_por_fornecedor_by_id_api_view(self, mock_diario_objects, mock_fornecedor_objects):
        mock_fornecedor = MagicMock()
        mock_fornecedor.id = 1
        mock_fornecedor.nome = "Fornecedor Teste"
        mock_fornecedor_objects.get.return_value = mock_fornecedor
        mock_diario = MagicMock()
        mock_diario.id = 1
        mock_diario.date = datetime(2024, 1, 1).date()
        mock_diario.url = "http://example.com"
        mock_diario.txt_url = "http://example.com/txt"
        mock_diario.excerpts = "Conteúdo do diário"
        mock_diario.contratacoes.all.return_value = []
        mock_qs = [mock_diario]
        mock_diario_objects.filter.return_value.distinct.return_value.order_by.return_value = mock_qs
        request = self.factory.post("/diarios-fornecedor/1/", {"nome": "Fornecedor Teste"}, format="json")
        view = DiariosPorFornecedorByIdAPIView.as_view()
        response = view(request, id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{
            "id": 1,
            "data_publicacao": "2024-01-01",
            "url": "http://example.com",
            "txt_url": "http://example.com/txt",
            "excerpts": "Conteúdo do diário",
            "contratacoes": []
        }])

if __name__ == "__main__":
    unittest.main()
