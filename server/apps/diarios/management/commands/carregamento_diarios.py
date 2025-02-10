from django.core.management.base import BaseCommand
from apps.diarios.services import Controladores


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.help = "Carrega os dados do dia dos diários."
        self.controlador = Controladores()

    def handle(self, *args, **kwargs):
        try:
            self.controlador.carregar_dados_diarios()
            print("Dados carregados com sucesso")
        except Exception as e:
            print(f"Erro ao carregar os dados: {str(e)}")
