import unittest
from unittest.mock import patch, Mock, mock_open
from apps.diarios.services import Controladores


class TestServices(unittest.TestCase):
    
    def setUp(self):
        self.controlador = Controladores()

    @patch("apps.diarios.services.requests.get")
    def test_processar_diarios_com_sucesso(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.iter_content = lambda chunk_size: [b"Mocked content"]
        mock_get.return_value = mock_response

        diarios_mock = [{
            "date": "2024-01-01",
            "url": "https://mock-url.com/diario.pdf",
            "txt_url": "https://mock-url.com/diario.txt",
            "edicao": "Extraordinária",
            "edicao_extra": True,
            "resumo": "",
        }]

        with patch("builtins.open", mock_open(read_data="Conteúdo do diário")):
            resultados = self.controlador.processar_diarios(diarios_mock)

        self.assertGreater(len(resultados), 0)
        self.assertEqual(resultados[0]["date"], "2024-01-01")

    @patch("apps.diarios.services.requests.get")
    def test_buscar_diarios_maceio_falha_requisicao(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            Controladores.buscar_diarios_maceio("termo", "2024-01-01", "2024-01-31")

        self.assertIn("Erro ao buscar diários", str(context.exception))
        self.assertIn("404 Not Found", str(context.exception))

    def test_processar_diarios_sem_diarios(self):
        resultados = self.controlador.processar_diarios([])
        self.assertEqual(resultados, [])

    def test_extrair_fornecedores_vazio(self):
        texto_mock = ""
        fornecedores = self.controlador.extrair_fornecedores(texto_mock)
        self.assertEqual(len(fornecedores), 0)

    def test_extrair_valores_sem_valores(self):
        texto_mock = "Não há valores monetários neste texto."
        valores = self.controlador.extrair_valores(texto_mock)
        self.assertEqual(valores, [])

    def test_converter_para_float_valor_completo(self):
        resultado = self.controlador.converter_para_float("R$ 1.234,56")
        self.assertEqual(resultado, 1234.56)

    def test_converter_para_float_valor_simples(self):
        resultado = self.controlador.converter_para_float("R$ 56,78")
        self.assertEqual(resultado, 56.78)

    def test_converter_para_float_valor_invalido(self):
        with self.assertRaises(ValueError):
            self.controlador.converter_para_float("Valor inválido")

    @patch("os.listdir")
    def test_limpar_diretorio_sem_arquivos(self, mock_listdir):
        mock_listdir.return_value = []
        self.controlador.limpar_diretorio("diarios_download")
        self.assertEqual(mock_listdir.call_count, 1)
        

if __name__ == "__main__":
    unittest.main()
