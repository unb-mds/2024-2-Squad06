from django.urls import path
from .views import  DiariosPorFornecedorByIdAPIView, FornecedorByNameAPIView, FornecedoresListAPIView, RequisicaoAPIView, FiltragemView

urlpatterns = [
    path("requisicao/", RequisicaoAPIView.as_view(), name="requisicao"),
    path('filtragem/', FiltragemView.as_view(), name='filtragem'),
    path("fornecedores/", FornecedoresListAPIView.as_view(), name="fornecedores"),
    path("fornecedor/", FornecedorByNameAPIView.as_view(), name="fornecedor-by-name"),
    path("diarios-fornecedor/<int:id>/", DiariosPorFornecedorByIdAPIView.as_view(), name="diarios-fornecedor-by-id"),
]

