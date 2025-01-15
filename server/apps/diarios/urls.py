from django.urls import path
from .views import BuscarDiariosAPIView, GetGazettesAPIView

urlpatterns = [
    path("buscar/", BuscarDiariosAPIView.as_view(), name="buscar_diarios"),
    path("getGazettes/", GetGazettesAPIView.as_view(), name="getGazettes"),
]
