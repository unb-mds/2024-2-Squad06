import unittest
from unittest.mock import patch, Mock
from .services import processar_diarios, extrair_fornecedores, extrair_valores

class TestDiarioServices(unittest.TestCase):
    @patch("apps.diarios.services.requests.get")
    def test_processar_diarios(self, mock_get):
        """Testa o processamento de diários sem fazer requisições reais."""
        # Mock da resposta do requests.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.iter_content = lambda chunk_size: [b"Mocked content"]
        mock_get.return_value = mock_response

        diarios_mock = [{
            "date": "2024-01-01",
            "url": "https://mock-url.com/diario.pdf",
            "txt_url": "https://mock-url.com/diario.txt",
            "edition": "Extraordinária",
            "is_extra_edition": True,
            "excerpts": "",
        }]

        resultados = processar_diarios(diarios_mock)

        # Testa se ao menos um diário foi processado
        self.assertGreater(len(resultados), 0)

    def test_extrair_fornecedores(self):
        """Testa a extração básica de fornecedores."""
        texto_mock = """
        Fornecedor: Empresa A
        CNPJ: 00.000.000/0000-00
        """

        fornecedores = extrair_fornecedores(texto_mock)

        # Testa se ao menos um fornecedor foi extraído
        self.assertIn("00.000.000/0000-00", fornecedores)
        self.assertEqual(fornecedores["00.000.000/0000-00"]["nome"], "Empresa A")

    def test_extrair_valores(self):
        """Testa a extração básica de valores monetários."""
        texto_mock = "Valor total: R$ 1.000,00"
        valores = extrair_valores(texto_mock)

        # Testa se ao menos um valor foi extraído
        self.assertIn("R$ 1.000,00", valores)

if __name__ == "__main__":
    unittest.main()
