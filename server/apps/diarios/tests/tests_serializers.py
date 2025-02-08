import unittest
from unittest.mock import MagicMock
from datetime import date
from apps.diarios.serializers import FornecedorSerializer, ContratacaoSerializer, DiarioSerializer

class SerializerTestCase(unittest.TestCase):
    def test_fornecedor_serializer(self):
        fornecedor_mock = MagicMock(nome='Fornecedor X', cnpj='12.345.678/0001-99', contract_count=5)
        serializer = FornecedorSerializer(instance=fornecedor_mock)
        
        expected_data = {
            'nome': 'Fornecedor X',
            'cnpj': '12.345.678/0001-99',
            'contract_count': 5
        }
        self.assertEqual(serializer.data, expected_data)

    def test_contratacao_serializer(self):
        fornecedor_mock = MagicMock(nome='Fornecedor X', cnpj='12.345.678/0001-99', contract_count=5)
        contratacao_mock = MagicMock(valor_mensal=10000.00, valor_anual=120000.00, vigencia='12 meses', data_assinatura=date(2024, 1, 1), fornecedor=fornecedor_mock)
        serializer = ContratacaoSerializer(instance=contratacao_mock)
        
        expected_data = {
            'valor_mensal': '10000.00', 
            'valor_anual': '120000.00', 
            'vigencia': '12 meses',
            'data_assinatura': '2024-01-01',
            'fornecedor': {
                'nome': 'Fornecedor X',
                'cnpj': '12.345.678/0001-99',
                'contract_count': 5
            }
        }
        self.assertEqual(serializer.data, expected_data)
    
    def test_diario_serializer(self):
        contratacao_mock = MagicMock(valor_mensal=10000.00, valor_anual=120000.00, vigencia='12 meses', data_assinatura=date(2024, 1, 1), fornecedor=MagicMock(nome='Fornecedor X', cnpj='12.345.678/0001-99', contract_count=5))
        diario_mock = MagicMock(date=date(2024, 2, 1), url='https://example.com', excerpts='Texto de exemplo', txt_url='https://example.com/texto', contratacao=[contratacao_mock])
        serializer = DiarioSerializer(instance=diario_mock)
        
        expected_data = {
            'date': '2024-02-01',
            'url': 'https://example.com',
            'excerpts': 'Texto de exemplo',
            'txt_url': 'https://example.com/texto',
            'contratacao': [
                {
                    'valor_mensal': '10000.00', 
                    'valor_anual': '120000.00', 
                    'vigencia': '12 meses',
                    'data_assinatura': '2024-01-01',
                    'fornecedor': {
                        'nome': 'Fornecedor X',
                        'cnpj': '12.345.678/0001-99',
                        'contract_count': 5
                    }
                }
            ]
        }

        self.assertEqual(serializer.data, expected_data)

if __name__ == '__main__':
    unittest.main()