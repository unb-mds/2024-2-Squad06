from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .serializers import DiarioSerializer
from .models import Diario
from .services import Controladores
from rest_framework.generics import ListAPIView


class BuscarDiariosAPIView(APIView):

    def __init__(self):
        super().__init__()
        self.controlador = Controladores()

    def get(self, request):
        query = request.GET.get("query", "licitação,contratação")
        data_inicial = request.GET.get("data_inicial", "2024-01-01")
        data_final = request.GET.get("data_final", datetime.today().strftime("%Y-%m-%d"))

        try:
            # Conversão das datas
            data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")
            data_final = datetime.strptime(data_final, "%Y-%m-%d")
            resultados = []

            # Busca iterando entre intervalos de 15 dias
            while data_inicial <= data_final:
                diarios = self.controlador.buscar_diarios_maceio(
                    query,
                    data_inicial.strftime("%Y-%m-%d"),
                    (data_inicial + timedelta(days=15)).strftime("%Y-%m-%d"),
                )
                # Processar os diários encontrados
                resultados.extend(self.controlador.processar_diarios(diarios))
                # Avançar para o próximo intervalo de 15 dias
                data_inicial += timedelta(days=15)

            return Response({"diarios": resultados}, status=status.HTTP_200_OK)

        except ValueError as ve:
            return Response({"erro": f"Datas inválidas: {ve}"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetGazettesAPIView(ListAPIView):
    queryset = Diario.objects.all()
    serializer_class = DiarioSerializer
