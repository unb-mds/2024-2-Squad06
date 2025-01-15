from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .services import buscar_diarios_maceio, processar_diarios
from .serializers import DiarioSerializer
from .models import Diario

class BuscarDiariosAPIView(APIView):
    def get(self, request):
        query = request.GET.get("query", "licitação,contratação")
        data_inicial = datetime.strptime(request.GET.get("data_inicial", "2024-01-01"), "%Y-%m-%d")
        data_final = datetime.strptime(request.GET.get("data_final", datetime.today().strftime("%Y-%m-%d")), "%Y-%m-%d")
        
        try:
            resultados = []
            
            while data_inicial <= data_final:
                published_since = data_inicial.strftime("%Y-%m-%d")
                published_until = (data_inicial + timedelta(days=15)).strftime("%Y-%m-%d")
                
                diarios = buscar_diarios_maceio(query, published_since, published_until)
                resultados_parciais = processar_diarios(diarios)
                resultados.extend(resultados_parciais)
                
                data_inicial += timedelta(days=10)

            return Response({"diarios": resultados}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetGazettesAPIView(ListAPIView):
    queryset = Diario.objects.all()
    serializer_class = DiarioSerializer