from django.db import models

class Diario(models.Model):
    date = models.DateField()
    url = models.URLField()
    excerpts = models.TextField(blank=True)
    edition = models.CharField(max_length=50)
    is_extra_edition = models.BooleanField(default=False)
    txt_url = models.URLField()

    @classmethod
    def get_valores_salvos(cls):
        diarios = cls.objects.all()
        resultados = []
        for diario in diarios:
            fornecedores = diario.fornecedores.all().values("nome", "cnpj", "contratacoes")
            resultados.append({
                "date": diario.date,
                "url": diario.url,
                "excerpts": diario.excerpts,
                "edition": diario.edition,
                "is_extra_edition": diario.is_extra_edition,
                "txt_url": diario.txt_url,
                "contratacoes": list(fornecedores),
                "fornecedores": list(fornecedores),
            })
        return resultados

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    diario = models.ForeignKey(Diario, related_name='fornecedores', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Contratacao(models.Model):
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_anual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vigencia = models.CharField(max_length=100, null=True, blank=True)
    diario = models.ForeignKey(Diario, related_name='contratacoes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Contratação de {self.fornecedor.nome} (Vigência: {self.vigencia})"
