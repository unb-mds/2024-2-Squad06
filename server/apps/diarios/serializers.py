from rest_framework import serializers
from .models import Diario, Fornecedor, Contratacao


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = [
            'nome',
            'cnpj',
        ]


class ContratacaoSerializer(serializers.ModelSerializer):
    fornecedor = FornecedorSerializer(read_only=True)

    class Meta:
        model = Contratacao
        fields = [
            'valor_mensal',
            'valor_anual',
            'vigencia',
            'fornecedor',
        ]


class DiarioSerializer(serializers.ModelSerializer):
    contratacao = ContratacaoSerializer(many= True, read_only=True)

    class Meta:
        model = Diario
        fields = [
            'date',
            'url',
            'excerpts',
            'txt_url',
            'contratacao',
        ]
