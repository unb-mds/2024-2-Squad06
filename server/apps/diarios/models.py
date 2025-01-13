from django.db import models

class Diario(models.Model):
    date = models.DateField()
    url = models.URLField()
    excerpts = models.TextField(blank=True)
    edition = models.CharField(max_length=50)
    is_extra_edition = models.BooleanField(default=False)
    txt_url = models.URLField()
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)
    
    @classmethod
    def get_valores_salvos(cls):
        # método para retornar os valores salvos
        diarios = cls.objects.all()
        resultados = []
        for diario in diarios:
            fornecedores = diario.fornecedores.all().values("nome", "cnpj", "ocorrencias")
            resultados.append({
                "date": diario.date,
                "url": diario.url,
                "excerpts": diario.excerpts,
                "edition": diario.edition,
                "is_extra_edition": diario.is_extra_edition,
                "txt_url": diario.txt_url,
                "valor_final": diario.valor_final,
                "fornecedores": list(fornecedores)
            })
        return resultados

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    diario = models.ForeignKey(Diario, related_name='fornecedores', on_delete=models.CASCADE)