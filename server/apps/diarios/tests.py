import unittest
from unittest.mock import patch, Mock
from apps.diarios.services import Controladores

class TestServices(unittest.TestCase):
    
    def __init__(self):
        self.controlador = Controladores()

    @patch("apps.diarios.services.requests.get")  
    def test_processar_diarios(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.iter_content = lambda chunk_size: [b"Mocked content"]
        mock_get.return_value = mock_response

        diarios_mock = [{
            "data": "2024-01-01",
            "url": "https://mock-url.com/diario.pdf",
            "txt_url": "https://mock-url.com/diario.txt",
            "edicao": "Extraordinária",
            "edicao_extra": True,
            "resumo": "",
        }]

        resultados = self.controlador.processar_diarios(diarios_mock)

        self.assertGreater(len(resultados), 0)

    def test_extrair_fornecedores(self):
        texto_mock = """
        Fornecedor: Empresa A
        CNPJ: 00.000.000/0000-00
        """

        fornecedores = self.controlador.extrair_fornecedores(texto_mock)

        self.assertIn("00.000.000/0000-00", fornecedores)
        self.assertEqual(fornecedores["00.000.000/0000-00"]["nome"], "Empresa A")

    def test_extrair_valores(self):
        texto_mock = "Valor total: R$ 1.000,00"
        valores = self.controlador.extrair_valores(texto_mock)

        self.assertIn("R$ 1.000,00", valores)

if __name__ == "__main__":
    unittest.main()
