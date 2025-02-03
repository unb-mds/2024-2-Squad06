import pytest
from django.urls import reverse, resolve

def test_buscar_diarios_url():
    url = reverse("buscar_diarios")
    resolver = resolve(url)
    assert resolver.view_name == "buscar_diarios"

def test_get_gazettes_url():
    url = reverse("getGazettes")
    resolver = resolve(url)
    assert resolver.view_name == "getGazettes"
