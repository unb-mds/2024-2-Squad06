from django.urls import path
from .views import RequisicaoAPIView, FiltragemView

urlpatterns = [
    path("requisicao/", RequisicaoAPIView.as_view(), name="requisicao"),
    path('filtragem/', FiltragemView.as_view(), name='filtragem'),
]
