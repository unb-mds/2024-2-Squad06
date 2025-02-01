from django.core.management.base import BaseCommand
from apps.diarios.services import Controladores  

class Command(BaseCommand):
    def __init__(self):
        self.help = "Carrega os dados semanais dos diários."
        self.controlador = Controladores()

    def handle(self, *args, **kwargs):
        try:
            self.controlador.carregar_dados_semanais()
            print('Dados semanais carregados com sucesso')
        except Exception as e:
            print(f'Erro ao carregar os dados semanais: {str(e)}')
