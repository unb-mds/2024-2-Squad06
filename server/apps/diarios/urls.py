from django.urls import path
from .views import buscar_diarios,getGazettes

urlpatterns = [
    path("buscar/", buscar_diarios, name="buscar_diarios"),
    path("getGazettes/", getGazettes, name="getGazettes"),
]
