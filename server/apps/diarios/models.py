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
        #método para retornar os valores salvos
        return list(cls.objects.values(
            "date", "url", "excerpts", "edition", "is_extra_edition", "txt_url", "valor_final"
        ))
