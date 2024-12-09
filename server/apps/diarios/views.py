from django.http import JsonResponse
from datetime import datetime, timedelta
from .services import buscar_diarios_maceio, processar_diarios

def buscar_diarios(request):
    query = request.GET.get("query", "licitação")
    data_inicial = datetime.strptime(request.GET.get("data_inicial", "2024-01-01"), "%Y-%m-%d")
    data_final = datetime.strptime(request.GET.get("data_final", "2024-12-31"), "%Y-%m-%d")
    
    try:
        resultados = []
        # criei esse loop para que fosse possivel mostrar os valores encontrados em um intervalo de tempo
        # antes baixava só de 10 em 10        
        while data_inicial <= data_final:
            published_since = data_inicial.strftime("%Y-%m-%d")
            published_until = (data_inicial + timedelta(days=30)).strftime("%Y-%m-%d")
            
            diarios = buscar_diarios_maceio(query, published_since, published_until)
            resultados.extend(processar_diarios(diarios))
            
            data_inicial += timedelta(days=31)  # Avança para o próximo mês
        
        return JsonResponse({"valores_encontrados": resultados})
    except Exception as e:
        return JsonResponse({"erro": str(e)}, status=500)