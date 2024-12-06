from django.urls import path
from apps.gastos_publicos.controllers.example_controller import example_view

urlpatterns = [
    path('example/', example_view, name='example'),
]
