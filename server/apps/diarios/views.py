from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .models import Diario
from .services import Controladores
from django.http import JsonResponse
from .models import Fornecedor, Diario


class RequisicaoAPIView(APIView):
    def __init__(self):
        super().__init__()
        self.controlador = Controladores()

    def get(self, request):
        query = request.GET.get("query", "contratação")
        data_inicial = request.GET.get("data_inicial", "2024-01-01")
        data_final = request.GET.get("data_final", datetime.today().strftime("%Y-%m-%d"))

        try:
            data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")
            data_final = datetime.strptime(data_final, "%Y-%m-%d")
            resultados = []

            while data_inicial <= data_final:
                diarios = self.controlador.buscar_diarios_maceio(
                    query,
                    data_inicial.strftime("%Y-%m-%d"),
                    (data_inicial + timedelta(days=15)).strftime("%Y-%m-%d"),
                )
                resultados.extend(self.controlador.processar_diarios(diarios))
                data_inicial += timedelta(days=15)

            return Response({"diarios": resultados}, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({"erro": f"Datas inválidas: {ve}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class FiltragemView(APIView):
    def get(self, request):
        data_publicacao = request.GET.get('data_publicacao')
        data_assinatura = request.GET.get('data_assinatura') 
        valor_mensal = request.GET.get('valor_mensal')
        valor_anual = request.GET.get('valor_anual')
        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            page = 1

        qs = Diario.objects.all()

        if data_publicacao:
            try:
                pub_date = datetime.strptime(data_publicacao, "%Y-%m-%d").date()
                qs = qs.filter(date=pub_date)
            except ValueError:
                return JsonResponse({"error": "Data de publicação inválida. Use o formato YYYY-MM-DD."}, status=400)

        if data_assinatura:
            try:
                ass_date = datetime.strptime(data_assinatura, "%Y-%m-%d").date()
                qs = qs.filter(contratacoes__data_assinatura=ass_date)
            except ValueError:
                return JsonResponse({"error": "Data de assinatura inválida. Use o formato YYYY-MM-DD."}, status=400)

        if valor_mensal:
            try:
                valor_mensal = float(valor_mensal)
                qs = qs.filter(contratacoes__valor_mensal=valor_mensal)
            except ValueError:
                return JsonResponse({"error": "Valor mensal inválido."}, status=400)

        if valor_anual:
            try:
                valor_anual = float(valor_anual)
                qs = qs.filter(contratacoes__valor_anual=valor_anual)
            except ValueError:
                return JsonResponse({"error": "Valor anual inválido."}, status=400)
        qs = qs.distinct().order_by('-id')

        start = (page - 1) * 9
        end = start + 9
        diarios_paginados = qs[start:end]

        resultado = []
        for diario in diarios_paginados:
            diario_data = {
                'id': diario.id,
                'data_publicacao': diario.date.strftime('%Y-%m-%d') if diario.date else None,
                'url': diario.url,
                'txt_url': diario.txt_url,
                'excerpts': diario.excerpts,
                'contratacoes': []
            }
            for contratacao in diario.contratacoes.all():
                contrato_data = {
                    'id': contratacao.id,
                    'valor_mensal': contratacao.valor_mensal,
                    'valor_anual': contratacao.valor_anual,
                    'data_assinatura': contratacao.data_assinatura.strftime('%Y-%m-%d') if contratacao.data_assinatura else None,
                    'vigencia': contratacao.vigencia,
                }
                diario_data['contratacoes'].append(contrato_data)
            resultado.append(diario_data)

        return JsonResponse(resultado, safe=False, status=200)

class DiariosPorFornecedorAPIView(APIView):
    def post(self, request):
        # Obtém o nome do fornecedor enviado no body da requisição
        fornecedor_nome = request.data.get('nome')
        if not fornecedor_nome:
            return Response({"error": "Nome do fornecedor não fornecido."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Busca o fornecedor pelo nome
            fornecedor = Fornecedor.objects.get(nome=fornecedor_nome)
        except Fornecedor.DoesNotExist:
            return Response({"error": "Fornecedor não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        # Filtra os Diários que possuam alguma contratação com esse fornecedor
        diarios = Diario.objects.filter(contratacoes__fornecedor=fornecedor).distinct()

        # Monta a resposta com as informações dos diários encontrados
        resultado = []
        for diario in diarios:
            diario_data = {
                'id': diario.id,
                'data_publicacao': diario.date.strftime('%Y-%m-%d') if diario.date else None,
                'url': diario.url,
                'txt_url': diario.txt_url,
                'excerpts': diario.excerpts,
                'contratacoes': []
            }
            # Filtra as contratações deste diário que correspondem ao fornecedor buscado
            contratacoes = diario.contratacoes.filter(fornecedor=fornecedor)
            for contratacao in contratacoes:
                contrato_data = {
                    'id': contratacao.id,
                    'valor_mensal': contratacao.valor_mensal,
                    'valor_anual': contratacao.valor_anual,
                    'data_assinatura': contratacao.data_assinatura.strftime('%Y-%m-%d') if contratacao.data_assinatura else None,
                    'vigencia': contratacao.vigencia,
                }
                diario_data['contratacoes'].append(contrato_data)
            resultado.append(diario_data)
        
        return Response(resultado, status=status.HTTP_200_OK)