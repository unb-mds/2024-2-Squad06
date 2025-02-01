from django.urls import path
from .views import RequisicaoAPIView, CarregarDadosSemanaisAPIView

urlpatterns = [
    path("requisicao/", RequisicaoAPIView.as_view(), name="requisicao"), 
    path('carregar-dados-semanais/', CarregarDadosSemanaisAPIView.as_view(), name='carregar-dados-semanais'),
]
