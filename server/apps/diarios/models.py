from django.db import models

class Diario(models.Model):
    date = models.DateField()
    url = models.URLField()
    edition = models.CharField(max_length=50)
    is_extra_edition = models.BooleanField(default=False)
    txt_url = models.URLField()
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)
