from django.test import SimpleTestCase
from unittest.mock import patch, MagicMock
from datetime import date
from apps.diarios.models import Fornecedor, Contratacao, Diario


class FornecedorModelTest(SimpleTestCase):
    def test_fornecedor_str(self):
        fornecedor = Fornecedor(nome="Fornecedor Teste", cnpj="00.000.000/0001-00")
        self.assertEqual(str(fornecedor), "Fornecedor Teste")


class ContratacaoModelTest(SimpleTestCase):
    def test_contratacao_str(self):
        fornecedor = Fornecedor(nome="Fornecedor Teste", cnpj="00.000.000/0001-00")
        contratacao = Contratacao(vigencia="2024", fornecedor=fornecedor)
        expected_str = f"Contratação de {fornecedor.nome} (Vigência: 2024)"
        self.assertEqual(str(contratacao), expected_str)


class DiarioModelTest(SimpleTestCase):

    @patch("apps.diarios.models.Diario.objects")
    @patch("apps.diarios.models.Contratacao.objects")
    def test_get_valores_salvos_vazio(
        self, mock_contratacao_objects, mock_diario_objects
    ):
        mock_diario_objects.all.return_value = []
        resultados = Diario.get_valores_salvos()
        self.assertEqual(resultados, [])

    @patch("apps.diarios.models.Diario.objects")
    @patch("apps.diarios.models.Contratacao.objects")
    def test_get_valores_salvos_com_dados(
        self, mock_contratacao_objects, mock_diario_objects
    ):
        mock_fornecedor = MagicMock()
        mock_fornecedor.nome = "Fornecedor Teste"
        mock_fornecedor.cnpj = "00.000.000/0001-00"

        mock_contratacao = MagicMock()
        mock_contratacao.valor_mensal = 200.00
        mock_contratacao.valor_anual = 2400.00
        mock_contratacao.vigencia = "2025"
        mock_contratacao.fornecedor = mock_fornecedor

        mock_query = MagicMock()
        mock_query.values.return_value = [
            {
                "valor_mensal": 200.00,
                "valor_anual": 2400.00,
                "vigencia": "2025",
                "fornecedor": mock_fornecedor,
            }
        ]

        mock_diario = MagicMock()
        mock_diario.date = date(2025, 1, 1)
        mock_diario.url = "https://example.com"
        mock_diario.excerpts = "Trecho de exemplo"
        mock_diario.txt_url = "https://example.com/text.txt"
        mock_diario.contratacao.all.return_value = mock_query

        mock_diario_objects.all.return_value = [mock_diario]

        with patch(
            "apps.diarios.models.Contratacao", new=MagicMock()
        ) as FakeContratacao:
            FakeContratacao.__iter__.return_value = iter([mock_contratacao])
            resultados = Diario.get_valores_salvos()

        self.assertEqual(len(resultados), 1)
        diario_resultado = resultados[0]
        self.assertEqual(diario_resultado["date"], mock_diario.date)
        self.assertEqual(diario_resultado["url"], mock_diario.url)
        self.assertEqual(diario_resultado["excerpts"], mock_diario.excerpts)
        self.assertEqual(diario_resultado["txt_url"], mock_diario.txt_url)
        self.assertEqual(diario_resultado["contratacoes"], [mock_contratacao])
