from django.urls import path
from .views import RequisicaoAPIView

urlpatterns = [
    path("requisicao/", RequisicaoAPIView.as_view(), name="requisicao"),
]
