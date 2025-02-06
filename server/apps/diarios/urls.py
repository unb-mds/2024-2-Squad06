from django.urls import path
from .views import  DiariosPorFornecedorByIdAPIView, FornecedorByNameAPIView, FornecedoresListAPIView, RequisicaoAPIView, DiariosView

urlpatterns = [
    path("requisicao/", RequisicaoAPIView.as_view(), name="requisicao"),
    path('get-diarios/', DiariosView.as_view(), name='Diarios'),
    path("fornecedores/", FornecedoresListAPIView.as_view(), name="fornecedores"),
    path("fornecedor/", FornecedorByNameAPIView.as_view(), name="fornecedor-by-name"),
    path("diarios-fornecedor/<int:id>/", DiariosPorFornecedorByIdAPIView.as_view(), name="diarios-fornecedor-by-id"),
]

