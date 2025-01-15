from rest_framework import serializers
from .models import Diario, Fornecedor

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj']

class DiarioSerializer(serializers.ModelSerializer):
    fornecedores = FornecedorSerializer(many=True, read_only=True)

    class Meta:
        model = Diario
        fields = ['date', 'url', 'excerpts', 'edition', 'is_extra_edition', 'txt_url', 'valor_final', 'fornecedores']
