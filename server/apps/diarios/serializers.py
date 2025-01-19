from rest_framework import serializers
from .models import Diario, Fornecedor, Contratacao

class ContratacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratacao
        fields = [
            'valor_mensal',
            'valor_anual',
            'vigencia',
            'fornecedor'
        ]

class FornecedorSerializer(serializers.ModelSerializer):
    contratacoes = ContratacaoSerializer(many=True, read_only=True)  # Relacionamento com Contratacao
    class Meta:
        model = Fornecedor
        fields = [
            'nome',
            'cnpj',
            'contratacoes',
        ]

class DiarioSerializer(serializers.ModelSerializer):
    fornecedores = FornecedorSerializer(many=True, read_only=True)  # Relacionamento com Fornecedor
    class Meta:
        model = Diario
        fields = [
            'date',
            'url',
            'excerpts',
            'edition',
            'is_extra_edition',
            'txt_url',
            'fornecedores',
            'contratacoes',
        ]
