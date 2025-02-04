import pytest
import os
# import re
from apps.diarios.services import Controladores, DIRETORIO_DOWNLOAD
from collections import defaultdict

@pytest.fixture
def controlador():
    return Controladores()

def test_converter_para_float_happy(controlador):
    resultado = controlador.converter_para_float("R$ 1.234,56")
    assert resultado == 1234.56

def test_converter_para_float_invalido(controlador):
    with pytest.raises(ValueError):
        controlador.converter_para_float("Valor inválido")

def test_extrair_info_contratos_happy():
    texto = "VIGÊNCIA: 12"
    contratos = Controladores.extrair_info_contratos(texto)
    assert contratos == ["12 meses"]

def test_extrair_info_contratos_ruim():
    texto = "Sem informação de vigência"
    contratos = Controladores.extrair_info_contratos(texto)
    assert contratos == []

def test_extrair_fornecedores_happy():
    texto = "Fornecedor registrado: Empresa Teste\n00.000.000/0001-00\n1 de janeiro de 2020"
    fornecedores = Controladores.extrair_fornecedores(texto)
    # Verifica se existe uma chave com o CNPJ esperado
    assert "00.000.000/0001-00" in fornecedores
    info = fornecedores["00.000.000/0001-00"]
    assert info["nome"] == "Teste"
    assert info["data_assinatura"] == "1 de janeiro de 2020"

def test_extrair_fornecedores_ruim():
    texto = ""
    fornecedores = Controladores.extrair_fornecedores(texto)
    assert len(fornecedores) == 0

def test_converter_para_float_estatico_happy():
    resultado = Controladores.converter_para_float("R$ 56,78")
    assert resultado == 56.78

def test_converter_para_float_estatico_invalido():
    with pytest.raises(ValueError):
        Controladores.converter_para_float("abc")

def test_filtrar_publicacoes():
    texto = "CONTRATO\nAlgum conteúdo sem MULTA."
    blocos = Controladores.filtrar_publicacoes(texto)
    assert isinstance(blocos, list)

# Exemplo de teste para baixar_arquivo utilizando monkeypatch
def fake_iter_content(chunk_size):
    yield b"Conteudo Fake"

class FakeResponse:
    status_code = 200
    def iter_content(self, chunk_size):
        return fake_iter_content(chunk_size)
    def raise_for_status(self):
        pass

def fake_requests_get(url, stream=False):
    return FakeResponse()

def test_baixar_arquivo(monkeypatch, controlador):
    monkeypatch.setattr("apps.diarios.services.requests.get", fake_requests_get)
    nome_arquivo = "arquivo_fake.txt"
    caminho = controlador.baixar_arquivo("http://example.com/arquivo.txt", nome_arquivo)
    # Verifica se o arquivo foi criado com o conteúdo esperado.
    assert os.path.exists(caminho)
    with open(caminho, "rb") as f:
        conteudo = f.read()
        assert conteudo == b"Conteudo Fake"
    os.remove(caminho)  # Limpeza do arquivo gerado


def test_extrair_valores_happy(controlador):
    texto = """
    valor unitário R$ 1.234,56
    valor unitário R$ 2.345,67
    """
    resultado = controlador.extrair_valores(texto)
    assert resultado == 3579.23  # Soma dos valores unitários

def test_extrair_valores_sem_unitarios(controlador):
    texto = """
    Outro texto qualquer
    R$ 123,45
    """
    resultado = controlador.extrair_valores(texto)
    assert resultado == [123.45]  # Lista com o valor encontrado

def test_extrair_valores_vazio(controlador):
    texto = """
    Sem valores no texto
    """
    resultado = controlador.extrair_valores(texto)
    assert resultado == []

def test_converter_valor_happy(controlador):
    valor = "1.234,56"
    resultado = controlador.converter_valor(valor)
    assert resultado == 1234.56

def test_converter_valor_ponto(controlador):
    valor = "1234.56"
    resultado = controlador.converter_valor(valor)
    assert resultado == 123456.0

def test_converter_valor_virgula(controlador):
    valor = "1.234.567,89"
    resultado = controlador.converter_valor(valor)
    assert resultado == 1234567.89

def test_converter_valor_zero(controlador):
    valor = "0,00"
    resultado = controlador.converter_valor(valor)
    assert resultado == 0.0

def test_converter_valor_invalido(controlador):
    valor = "valor inválido"
    with pytest.raises(ValueError):
        controlador.converter_valor(valor)

def test_buscar_diarios_maceio_happy():
    querystring = "saúde"
    published_since = "2023-01-01"
    published_until = "2023-12-31"
    
    expected_response = {
        "gazettes": [
            {"title": "Diário 1", "date": "2023-01-15"},
            {"title": "Diário 2", "date": "2023-06-20"}
        ]
    }
    
    with patch('apps.diarios.services.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response
        
        response = buscar_diarios_maceio(querystring, published_since, published_until)
        assert response == expected_response["gazettes"]

def test_buscar_diarios_maceio_erro():
    querystring = "saúde"
    published_since = "2023-01-01"
    published_until = "2023-12-31"
    
    with patch('apps.diarios.services.requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.text = "Not Found"
        
        with pytest.raises(Exception) as exc_info:
            buscar_diarios_maceio(querystring, published_since, published_until)
        
        assert str(exc_info.value) == "Erro ao buscar diários: 404 Not Found"