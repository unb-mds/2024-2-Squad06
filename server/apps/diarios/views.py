from django.http import JsonResponse
from datetime import datetime, timedelta
from .services import buscar_diarios_maceio, processar_diarios, get_dados_salvos


def buscar_diarios(request):
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
        
        return JsonResponse({"diarios": resultados})
    except Exception as e:
        return JsonResponse({"erro": str(e)}, status=500)
    
def getGazettes(request):
    try:
        dados = get_dados_salvos()
        return JsonResponse({"dados": dados})
    except Exception as e:
        return JsonResponse({"erro": str(e)}, status=500)