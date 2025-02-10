import unittest
import json
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from rest_framework.test import APIRequestFactory
from rest_framework import status
from apps.diarios.views import (
    RequisicaoAPIView,
    DiariosView,
    FornecedoresListAPIView,
    FornecedorByNameAPIView,
    DiariosPorFornecedorByIdAPIView,
)
# Importações para simulação de exceções do ORM
from apps.diarios.models import Fornecedor

class TestViewsWithoutDatabase(unittest.TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    # ===============================
    # Testes para RequisicaoAPIView
    # ===============================
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

    @patch("apps.diarios.views.Controladores")
    def test_requisicao_api_view_invalid_dates(self, mock_controladores):
        # Testa quando data_inicial é inválida, disparando ValueError.
        request = self.factory.get(
            "/requisicao/",
            {
                "data_inicial": "invalid-date",
                "data_final": "2024-01-15"
            }
        )
        view = RequisicaoAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Datas inválidas", response.data.get("erro", ""))

    @patch("apps.diarios.views.Controladores")
    def test_requisicao_api_view_exception(self, mock_controladores):
        # Simula uma exceção inesperada na chamada do controlador.
        mock_controlador = mock_controladores.return_value
        mock_controlador.buscar_diarios_maceio.side_effect = Exception("Erro inesperado")
        request = self.factory.get(
            "/requisicao/",
            {
                "data_inicial": "2024-01-01",
                "data_final": "2024-01-15"
            }
        )
        view = RequisicaoAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data.get("erro"), "Erro inesperado")

    # ===============================
    # Testes para DiariosView
    # ===============================
    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_view(self, mock_diario_objects):
        mock_diario = MagicMock()
        mock_diario.id = 1
        mock_diario.date = datetime(2024, 1, 1).date()
        mock_diario.url = "http://example.com"
        mock_diario.txt_url = "http://example.com/txt"
        mock_diario.excerpts = "Conteúdo do diário"
        # Simula uma lista vazia de contratacoes
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

    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_view_invalid_data_publicacao(self, mock_diario_objects):
        # Testa o branch de data_publicacao inválida.
        request = self.factory.get("/diarios/", {"data_publicacao": "invalid-date"})
        view = DiariosView.as_view()
        response = view(request)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Data de publicação inválida", data.get("error", ""))

    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_view_invalid_data_assinatura(self, mock_diario_objects):
        # Testa o branch de data_assinatura inválida.
        request = self.factory.get("/diarios/", {"data_assinatura": "invalid-date"})
        view = DiariosView.as_view()
        response = view(request)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Data de assinatura inválida", data.get("error", ""))

    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_view_invalid_valor_mensal(self, mock_diario_objects):
        # Testa o branch de valor_mensal inválido.
        request = self.factory.get("/diarios/", {"valor_mensal": "not-a-number"})
        view = DiariosView.as_view()
        response = view(request)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Valor mensal inválido", data.get("error", ""))

    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_view_invalid_valor_anual(self, mock_diario_objects):
        # Testa o branch de valor_anual inválido.
        request = self.factory.get("/diarios/", {"valor_anual": "not-a-number"})
        view = DiariosView.as_view()
        response = view(request)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Valor anual inválido", data.get("error", ""))

    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_view_with_contratacoes(self, mock_diario_objects):
        # Testa o branch em que há contratacoes e o fornecedor tem nome com mais de 6 caracteres.
        mock_diario = MagicMock()
        mock_diario.id = 2
        mock_diario.date = datetime(2024, 1, 2).date()
        mock_diario.url = "http://example.org"
        mock_diario.txt_url = "http://example.org/txt"
        mock_diario.excerpts = "Diário com contrato"
        # Simula uma contratacao com fornecedor cujo nome tem mais de 6 caracteres.
        mock_contratacao = MagicMock()
        mock_contratacao.id = 10
        mock_contratacao.valor_mensal = 100.0
        mock_contratacao.valor_anual = 1200.0
        mock_contratacao.data_assinatura = datetime(2024, 1, 2).date()
        mock_contratacao.vigencia = "12 meses"
        mock_fornecedor = MagicMock()
        mock_fornecedor.nome = "FornecedorX"
        mock_fornecedor.cnpj = "11.111.111/1111-11"
        mock_fornecedor.id = 100
        mock_contratacao.fornecedor = mock_fornecedor
        mock_diario.contratacoes.all.return_value = [mock_contratacao]
        mock_qs = [mock_diario]
        mock_diario_objects.all.return_value.filter.return_value.distinct.return_value.order_by.return_value = mock_qs

        request = self.factory.get("/diarios/", {"data_publicacao": "2024-01-02"})
        view = DiariosView.as_view()
        response = view(request)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)
        diario_data = data[0]
        self.assertEqual(diario_data["id"], 2)
        self.assertEqual(len(diario_data["contratacoes"]), 1)
        contrato_data = diario_data["contratacoes"][0]
        self.assertEqual(contrato_data["id"], 10)
        self.assertEqual(contrato_data["valor_mensal"], 100.0)
        self.assertEqual(contrato_data["fornecedor"]["nome"], "FornecedorX")

    # =====================================
    # Testes para FornecedoresListAPIView
    # (O teste original já cobre este cenário)
    @patch("apps.diarios.views.Fornecedor.objects")
    def test_fornecedores_list_api_view(self, mock_fornecedor_objects):
        mock_fornecedor = MagicMock()
        mock_fornecedor.id = 1
        mock_fornecedor.nome = "Fornecedor Teste"
        mock_fornecedor.cnpj = "00.000.000/0001-00"
        # Simula o valor de contract_count (por exemplo, 1)
        mock_fornecedor.contract_count = 1
        mock_qs = [mock_fornecedor]
        mock_fornecedor_objects.annotate.return_value.filter.return_value.order_by.return_value = mock_qs
        request = self.factory.get("/fornecedores/")
        view = FornecedoresListAPIView.as_view()
        response = view(request)
        # Converte cada objeto serializado em dicionário
        result = [dict(item) for item in response.data]
        expected = [{
            "nome": "Fornecedor Teste",
            "cnpj": "00.000.000/0001-00",
            "contract_count": 1
        }]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, expected)

    # =====================================
    # Testes para FornecedorByNameAPIView
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
    def test_fornecedor_by_name_api_view_missing_nome(self, mock_fornecedor_objects):
        # Testa quando o nome não é fornecido na requisição.
        request = self.factory.post("/fornecedor/", {}, format="json")
        view = FornecedorByNameAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("error"), "Nome do fornecedor não fornecido.")

    @patch("apps.diarios.views.Fornecedor.objects")
    def test_fornecedor_by_name_api_view_multiple(self, mock_fornecedor_objects):
        # Simula o cenário de múltiplos fornecedores retornados.
        mock_fornecedor_objects.get.side_effect = Fornecedor.MultipleObjectsReturned
        fake_fornecedor1 = MagicMock()
        fake_fornecedor1.id = 1
        fake_fornecedor2 = MagicMock()
        fake_fornecedor2.id = 2
        # Simula que o filtro retorne os IDs [1, 2]
        mock_fornecedor_objects.filter.return_value.values_list.return_value = [1, 2]
        request = self.factory.post("/fornecedor/", {"nome": "Fornecedor Teste"}, format="json")
        view = FornecedorByNameAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"ids": [1, 2]})

    # =====================================
    # Testes para DiariosPorFornecedorByIdAPIView
    @patch("apps.diarios.views.Fornecedor.objects")
    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_por_fornecedor_by_id_api_view(self, mock_diario_objects, mock_fornecedor_objects):
        # Cenário padrão com dados válidos.
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

    @patch("apps.diarios.views.Fornecedor.objects")
    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_por_fornecedor_by_id_api_view_invalid_page(self, mock_diario_objects, mock_fornecedor_objects):
        # Testa quando o parâmetro 'page' não pode ser convertido para inteiro.
        mock_fornecedor = MagicMock()
        mock_fornecedor.id = 1
        mock_fornecedor.nome = "Fornecedor Teste"
        mock_fornecedor_objects.get.return_value = mock_fornecedor
        request = self.factory.post(
            "/diarios-fornecedor/1/", {"nome": "Fornecedor Teste", "page": "invalid"}, format="json"
        )
        view = DiariosPorFornecedorByIdAPIView.as_view()
        response = view(request, id=1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("error"), "Parâmetro 'page' inválido.")

    @patch("apps.diarios.views.Fornecedor.objects")
    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_por_fornecedor_by_id_api_view_fornecedor_not_found(self, mock_diario_objects, mock_fornecedor_objects):
        # Simula Fornecedor.DoesNotExist para id diferente de 0.
        mock_fornecedor_objects.get.side_effect = Fornecedor.DoesNotExist
        request = self.factory.post(
            "/diarios-fornecedor/999/", {"nome": "Fornecedor Inexistente"}, format="json"
        )
        view = DiariosPorFornecedorByIdAPIView.as_view()
        response = view(request, id=999)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.get("error"), "Fornecedor não encontrado.")

    @patch("apps.diarios.views.Fornecedor.objects")
    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_por_fornecedor_by_id_api_view_nome_mismatch(self, mock_diario_objects, mock_fornecedor_objects):
        # Testa quando o nome informado não corresponde ao fornecedor obtido.
        mock_fornecedor = MagicMock()
        mock_fornecedor.id = 1
        mock_fornecedor.nome = "Fornecedor Correto"
        mock_fornecedor_objects.get.return_value = mock_fornecedor
        request = self.factory.post(
            "/diarios-fornecedor/1/", {"nome": "Fornecedor Errado"}, format="json"
        )
        view = DiariosPorFornecedorByIdAPIView.as_view()
        response = view(request, id=1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("O nome fornecido não corresponde", response.data.get("error", ""))

    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_por_fornecedor_by_id_api_view_invalid_data_publicacao(self, mock_diario_objects):
        # Testa o branch id == 0 com data_publicacao inválida.
        request = self.factory.post(
            "/diarios-fornecedor/0/", {"data_publicacao": "invalid-date"}, format="json"
        )
        view = DiariosPorFornecedorByIdAPIView.as_view()
        response = view(request, id=0)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Data de publicação inválida", data.get("error", ""))

    @patch("apps.diarios.views.Diario.objects")
    def test_diarios_por_fornecedor_by_id_api_view_invalid_data_assinatura(self, mock_diario_objects):
        # Testa o branch id == 0 com data_assinatura inválida.
        request = self.factory.post(
            "/diarios-fornecedor/0/", {"data_assinatura": "invalid-date"}, format="json"
        )
        view = DiariosPorFornecedorByIdAPIView.as_view()
        response = view(request, id=0)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Data de assinatura inválida", data.get("error", ""))

if __name__ == "__main__":
    unittest.main()
