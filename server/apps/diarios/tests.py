from django.test import TestCase
from .models import Diario  # Certifique-se de que o caminho para models está correto

class DiarioTestCase(TestCase):
    def test_diarios_salvos(self):
        diarios = Diario.objects.all()  # Recupera todos os registros
        for diario in diarios:
            print(diario.date, diario.url, diario.valor_final)
