from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Contratacao(models.Model):
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_anual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vigencia = models.CharField(max_length=100, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, related_name='fornecedor',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Contratação de {self.fornecedor.nome} (Vigência: {self.vigencia})"
    
class Diario(models.Model):
    date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    excerpts = models.TextField(null=True, blank=True)
    txt_url = models.URLField(null=True, blank=True)
    contratacao = models.ForeignKey(Contratacao, related_name='contratacao',on_delete=models.CASCADE, null=True, blank=True)

    @classmethod
    def get_valores_salvos(cls):
        diarios = cls.objects.all()
        resultados = []
        for diario in diarios:
            contratacao = diario.contratacao.all().values("valor_mensal", "valor_anual", "vigencia", "fornecedor")
            resultados.append({
                "date": diario.date,
                "url": diario.url,
                "excerpts": diario.excerpts,
                "txt_url": diario.txt_url,
                "contratacao": list(Contratacao),
            })
        return resultados


