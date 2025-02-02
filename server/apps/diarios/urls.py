from django.urls import path
from .views import DiariosPorFornecedorAPIView, RequisicaoAPIView, FiltragemView

urlpatterns = [
    path("requisicao/", RequisicaoAPIView.as_view(), name="requisicao"),
    path('filtragem/', FiltragemView.as_view(), name='filtragem'),
    path('diarios-fornecedor/', DiariosPorFornecedorAPIView.as_view(), name='diarios-fornecedor'),
]
