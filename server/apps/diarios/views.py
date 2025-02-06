from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta

from django.http import JsonResponse
from django.db.models.functions import Length
from django.db.models import Count

from .serializers import FornecedorSerializer
from .models import Diario
from .services import Controladores
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
        


# views.py
class DiariosView(APIView):
    def get(self, request):
        data_publicacao = request.GET.get('data_publicacao')
        data_assinatura = request.GET.get('data_assinatura') 
        valor_mensal = request.GET.get('valor_mensal')
        valor_anual = request.GET.get('valor_anual')
        
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
        
        qs = qs.distinct().order_by('-date')
        qs = qs[:3]
        
        resultado = []
        for diario in qs:
            diario_data = {
                'id': diario.id,
                'data_publicacao': diario.date.strftime('%Y-%m-%d') if diario.date else None,
                'url': diario.url,
                'txt_url': diario.txt_url,
                'excerpts': diario.excerpts,
                'contratacoes': []
            }
            for contratacao in diario.contratacoes.all():
                if (len(contratacao.fornecedor.nome) > 6):
                    contrato_data = {
                        'id': contratacao.id,
                        'nome': contratacao.fornecedor.nome,
                        'cnpj': contratacao.fornecedor.cnpj,
                        'valor_mensal': contratacao.valor_mensal,
                        'valor_anual': contratacao.valor_anual,
                        'data_assinatura': contratacao.data_assinatura.strftime('%Y-%m-%d') if contratacao.data_assinatura else None,
                        'vigencia': contratacao.vigencia,
                    }
                    diario_data['contratacoes'].append(contrato_data)
            resultado.append(diario_data)
        
        return JsonResponse(resultado, safe=False, status=200)



class FornecedoresListAPIView(APIView):
    def get(self, request):
        fornecedores = Fornecedor.objects.annotate(
            nome_length=Length('nome'),
            contract_count=Count('fornecedor')
        ).filter(nome_length__gt=5).order_by('-contract_count')[:10]
        serializer = FornecedorSerializer(fornecedores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FornecedorByNameAPIView(APIView):
    def post(self, request):
        fornecedor_nome = request.data.get('nome')
        if not fornecedor_nome:
            return Response({"error": "Nome do fornecedor não fornecido."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            fornecedor = Fornecedor.objects.get(nome=fornecedor_nome)
            return Response({"id": fornecedor.id}, status=status.HTTP_200_OK)
        except Fornecedor.DoesNotExist:
            return Response({"error": "Fornecedor não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Fornecedor.MultipleObjectsReturned:
            fornecedores = Fornecedor.objects.filter(nome=fornecedor_nome)
            ids = list(fornecedores.values_list('id', flat=True))
            return Response({"ids": ids}, status=status.HTTP_200_OK)
        
class DiariosPorFornecedorByIdAPIView(APIView):
    def post(self, request, id):
        try:
            fornecedor = Fornecedor.objects.get(id=id)
        except Fornecedor.DoesNotExist:
            return Response({"error": "Fornecedor não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        nome_body = request.data.get('nome')
        data_assinatura_str = request.data.get('data_assinatura')
        data_publicacao_str = request.data.get('data_publicacao')
        
        if nome_body and nome_body != fornecedor.nome:
            return Response(
                {"error": "O nome fornecido não corresponde ao fornecedor com o id informado."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        diarios = Diario.objects.filter(contratacoes__fornecedor=fornecedor).distinct()
        
        if data_assinatura_str:
            try:
                data_assinatura_date = datetime.strptime(data_assinatura_str, "%Y-%m-%d").date()
                diarios = diarios.filter(contratacoes__data_assinatura=data_assinatura_date)
            except ValueError:
                return Response({"error": "Data de assinatura inválida. Use o formato YYYY-MM-DD."},
                                status=status.HTTP_400_BAD_REQUEST)
        
        if data_publicacao_str:
            try:
                data_publicacao_date = datetime.strptime(data_publicacao_str, "%Y-%m-%d").date()
                diarios = diarios.filter(date=data_publicacao_date)
            except ValueError:
                return Response({"error": "Data de publicação inválida. Use o formato YYYY-MM-DD."},
                                status=status.HTTP_400_BAD_REQUEST)
        
        resultado = []
        print(len(diarios))
        for diario in diarios:
            diario_data = {
                'id': diario.id,
                'data_publicacao': diario.date.strftime("%Y-%m-%d") if diario.date else None,
                'url': diario.url,
                'txt_url': diario.txt_url,
                'excerpts': diario.excerpts,
                'contratacoes': []
            }
            for contratacao in diario.contratacoes.all():
                if len(contratacao.fornecedor.nome) > 6:
                    contrato_data = {
                        'id': contratacao.id,
                        'valor_mensal': contratacao.valor_mensal,
                        'valor_anual': contratacao.valor_anual,
                        'data_assinatura': contratacao.data_assinatura.strftime("%Y-%m-%d") if contratacao.data_assinatura else None,
                        'vigencia': contratacao.vigencia,
                        'fornecedor': {
                            'id': contratacao.fornecedor.id if contratacao.fornecedor else None,
                            'nome': contratacao.fornecedor.nome if contratacao.fornecedor else None,
                            'cnpj': contratacao.fornecedor.cnpj if contratacao.fornecedor else None,
                        }
                    }
                    diario_data['contratacoes'].append(contrato_data)
            resultado.append(diario_data)
        
        return Response(resultado, status=status.HTTP_200_OK)