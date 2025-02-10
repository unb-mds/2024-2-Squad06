from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.diarios.views import (
    RequisicaoAPIView,
    DiariosView,
    FornecedoresListAPIView,
    FornecedorByNameAPIView,
    DiariosPorFornecedorByIdAPIView,
)


class TestUrls(SimpleTestCase):
    def test_requisicao_url_resolves(self):
        url = reverse("requisicao")
        self.assertEqual(resolve(url).func.view_class, RequisicaoAPIView)

    def test_diarios_url_resolves(self):
        url = reverse("Diarios")
        self.assertEqual(resolve(url).func.view_class, DiariosView)

    def test_fornecedores_url_resolves(self):
        url = reverse("fornecedores")
        self.assertEqual(resolve(url).func.view_class, FornecedoresListAPIView)

    def test_fornecedor_by_name_url_resolves(self):
        url = reverse("fornecedor-by-name")
        self.assertEqual(resolve(url).func.view_class, FornecedorByNameAPIView)

    def test_diarios_fornecedor_by_id_url_resolves(self):
        url = reverse("diarios-fornecedor-by-id", kwargs={"id": 1})
        self.assertEqual(resolve(url).func.view_class, DiariosPorFornecedorByIdAPIView)
