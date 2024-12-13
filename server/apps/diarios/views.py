from django.http import JsonResponse
from datetime import datetime, timedelta
from .services import buscar_diarios_maceio, processar_diarios, salvar_resultados_no_banco, get_dados_salvos

def buscar_diarios(request):
    query = request.GET.get("query", "licitação,contratação")
    data_inicial = datetime.strptime(request.GET.get("data_inicial", "2024-01-01"), "%Y-%m-%d")
    data_final = datetime.strptime(request.GET.get("data_final", "2024-12-31"), "%Y-%m-%d")
    
    try:
        resultados = []
        # criei esse loop para que fosse possivel mostrar os valores encontrados em um intervalo de tempo
        # antes baixava só de 10 em 10        
        while data_inicial <= data_final:
            published_since = data_inicial.strftime("%Y-%m-%d")
            published_until = (data_inicial + timedelta(days=15)).strftime("%Y-%m-%d")
            
            diarios = buscar_diarios_maceio(query, published_since, published_until)
            resultados.extend(processar_diarios(diarios))
            
            data_inicial += timedelta(days=10)  # Avança para o próximo mês
        
        salvar_resultados_no_banco(resultados)
        
        return JsonResponse({"dados": resultados})
    except Exception as e:
        return JsonResponse({"erro": str(e)}, status=500)
    
def getGazettes(request):
    try:
        dados = get_dados_salvos()
        return JsonResponse({"dados": dados})
    except Exception as e:
        return JsonResponse({"erro": str(e)}, status=500)