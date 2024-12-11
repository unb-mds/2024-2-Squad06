from django.urls import path
from .views import buscar_diarios

urlpatterns = [
    path("buscar/", buscar_diarios, name="buscar_diarios"),
]
