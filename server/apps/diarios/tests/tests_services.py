import unittest
from unittest.mock import patch, Mock, mock_open, MagicMock
import os
import sys
import io
from datetime import datetime
from apps.diarios.services import Controladores, DIRETORIO_DOWNLOAD, URL_BASE
from apps.diarios.models import Diario, Fornecedor, Contratacao


class TestServices(unittest.TestCase):

    def setUp(self):
        self.controlador = Controladores()

    @patch("apps.diarios.services.requests.get")
    def test_processar_diarios_com_sucesso(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.iter_content = lambda chunk_size: [b"Mocked content"]
        mock_get.return_value = mock_response

        diarios_mock = [
            {
                "date": "2024-01-01",
                "url": "https://mock-url.com/diario.pdf",
                "txt_url": "https://mock-url.com/diario.txt",
                "edicao": "Extraordinária",
                "edicao_extra": True,
                "resumo": "",
            }
        ]

        with patch("builtins.open", mock_open(read_data="Conteúdo do diário")):
            with patch.object(self.controlador, "salvar_banco_de_dados"), patch.object(
                self.controlador, "limpar_diretorio"
            ):
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

    @patch("apps.diarios.services.requests.get")
    def test_buscar_diarios_maceio_erro_mediano(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            Controladores.buscar_diarios_maceio("termo", "2024-01-01", "2024-01-31")

        self.assertIn("Erro ao buscar diários", str(context.exception))
        self.assertIn("500 Internal Server Error", str(context.exception))

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

    @patch("apps.diarios.services.requests.get")
    def test_baixar_arquivo_sucesso(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.iter_content = lambda chunk_size: [b"Mocked content"]
        mock_get.return_value = mock_response

        with patch("builtins.open", mock_open()) as mock_file:
            caminho_arquivo = self.controlador.baixar_arquivo(
                "https://mock-url.com/diario.txt", "diario.txt"
            )
            mock_file.assert_called_once_with(
                os.path.join("diarios_download", "diario.txt"), "wb"
            )
            self.assertEqual(
                caminho_arquivo, os.path.join("diarios_download", "diario.txt")
            )

    def test_associar_valores_a_contratos(self):
        texto_mock = "Contrato 1: R$ 1.000,00 e R$ 2.000,00. Fornecedor A. Contrato 2: R$ 3.000,00 e R$ 4.000,00. Fornecedor B."
        associacoes = self.controlador.associar_valores_a_contratos(texto_mock)
        self.assertEqual(len(associacoes), 2)
        self.assertEqual(associacoes[0]["valores"], ["R$ 1.000,00", "R$ 2.000,00"])
        self.assertEqual(associacoes[1]["valores"], ["R$ 3.000,00", "R$ 4.000,00"])

    def test_extrair_info_contratos(self):
        texto_mock = "VIGÊNCIA: 12 meses. Assinado em 01 de janeiro de 2024."
        contratos = self.controlador.extrair_info_contratos(texto_mock)
        self.assertEqual(len(contratos), 1)
        self.assertEqual(contratos[0]["vigencia"], "12 meses")
        self.assertEqual(contratos[0]["data_assinatura"], "2024-01-01")

    def test_filtrar_publicacoes(self):
        texto_mock = "SECRETARIA DE EDUCAÇÃO: Detalhes da secretaria. CONTRATO: Detalhes do contrato. INSTITUTO DE TESTE: Detalhes do instituto."
        blocos_contratos = self.controlador.filtrar_publicacoes(texto_mock)
        self.assertEqual(len(blocos_contratos), 3)

    def test_filtrar_publicacoes_erro_mediano(self):
        texto_mock = "INSTITUTO DE TESTE: Detalhes do instituto."
        blocos_contratos = self.controlador.filtrar_publicacoes(texto_mock)
        self.assertEqual(len(blocos_contratos), 1)

    def test_filtrar_publicacoes_erro_completo(self):
        texto_mock = ""
        blocos_contratos = self.controlador.filtrar_publicacoes(texto_mock)
        self.assertEqual(len(blocos_contratos), 0)

    def test_converter_valor(self):
        resultado = self.controlador.converter_valor("1.234,56")
        self.assertEqual(resultado, 1234.56)

    def test_extrair_valores_com_valor_numerico(self):
        texto_mock = "O valor total é R$ 1.234,56."
        resultado = self.controlador.extrair_valores(texto_mock)
        self.assertEqual(resultado, 1234.56)

    def test_extrair_valores_com_valores_unitarios(self):
        texto_mock = "valor unitário R$ 1.000,00"
        resultado = self.controlador.extrair_valores(texto_mock)
        self.assertEqual(resultado, 1000.0)

    @patch("apps.diarios.services.Controladores.baixar_arquivo")
    def test_processar_diarios_com_erro(self, mock_baixar):
        mock_baixar.side_effect = Exception("Erro de download")
        diarios_mock = [
            {
                "date": "2024-01-02",
                "url": "https://mock-url.com/diario.pdf",
                "txt_url": "https://mock-url.com/diario.txt",
                "edicao": "Normal",
                "edicao_extra": False,
                "resumo": "",
            }
        ]
        captured_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured_output
        with patch.object(self.controlador, "salvar_banco_de_dados"), patch.object(
            self.controlador, "limpar_diretorio"
        ):
            resultados = self.controlador.processar_diarios(diarios_mock)
        sys.stdout = old_stdout
        self.assertEqual(resultados, [])

    def test_processar_diarios_com_contratacoes(self):
        diario = {
            "date": "2024-01-03",
            "url": "https://mock-url.com/diario.pdf",
            "txt_url": "fake.txt",
            "excerpts": "Teste contratacoes",
        }
        with patch.object(self.controlador, "baixar_arquivo", return_value="fake.txt"):
            with patch("builtins.open", mock_open(read_data="dummy content")):
                self.controlador.filtrar_publicacoes = lambda txt: ["dummy bloco"]
                self.controlador.extrair_valores = lambda txt: 100.0
                self.controlador.extrair_fornecedores = lambda txt: {
                    "dummy": {"nome": "Fornecedor X", "cnpj": "123"}
                }
                self.controlador.extrair_info_contratos = lambda txt: [
                    {"vigencia": "2", "data_assinatura": "2024-01-01"}
                ]
                with patch.object(
                    self.controlador, "salvar_banco_de_dados"
                ), patch.object(self.controlador, "limpar_diretorio"):
                    resultados = self.controlador.processar_diarios([diario])
        self.assertEqual(len(resultados), 1)
        self.assertTrue(len(resultados[0]["contratacoes"]) > 0)

    @patch("apps.diarios.services.Diario")
    @patch("apps.diarios.services.Fornecedor")
    @patch("apps.diarios.services.Contratacao")
    def test_salvar_banco_de_dados_novo(
        self, mock_contratacao, mock_fornecedor, mock_diario
    ):
        dados = {
            "date": "2024-01-01",
            "url": "https://mock-url.com/diario.pdf",
            "txt_url": "https://mock-url.com/diario.txt",
            "excerpts": "Teste",
            "contratacoes": [
                {
                    "fornecedor": {"nome": "Fornecedor X", "cnpj": "123"},
                    "valores": {"mensal": 100.0, "anual": 1200.0},
                    "data_assinatura": "2024-01-01",
                    "vigencia": "2",
                }
            ],
        }
        mock_diario.objects.filter.return_value.first.return_value = None
        mock_fornecedor.objects.filter.return_value.first.return_value = None
        mock_diario.objects.create.return_value = MagicMock(
            contratacoes=MagicMock(add=lambda x: None)
        )
        self.controlador.salvar_banco_de_dados(dados)

    def test_salvar_banco_de_dados_url_none(self):
        dados = {
            "date": "2024-01-01",
            "txt_url": "https://mock-url.com/diario.txt",
            "excerpts": "Teste",
            "contratacoes": [],
        }
        with self.assertRaises(ValueError):
            self.controlador.salvar_banco_de_dados(dados)

    @patch("apps.diarios.services.Controladores.buscar_diarios_maceio")
    @patch("apps.diarios.services.Diario")
    def test_carregar_dados_diarios_sucesso(self, mock_diario, mock_buscar):
        hoje = datetime.today().date()
        fake_diario = {"txt_url": "fake_url"}
        mock_diario.objects.filter.return_value.exists.return_value = False
        mock_buscar.return_value = [fake_diario]
        with patch.object(
            self.controlador, "processar_diarios", return_value=["resultado"]
        ):
            with patch("builtins.print") as mock_print:
                self.controlador.carregar_dados_diarios()
                mock_print.assert_called_with(
                    "Carregamento concluído com sucesso: 1 diários processados."
                )

    @patch("apps.diarios.services.Controladores.buscar_diarios_maceio")
    def test_carregar_dados_diarios_erro(self, mock_buscar):
        mock_buscar.side_effect = Exception("Erro de busca")
        with patch("builtins.print") as mock_print:
            self.controlador.carregar_dados_diarios()
            mock_print.assert_called_with("Erro ao carregar dados: Erro de busca")


if __name__ == "__main__":
    unittest.main()
