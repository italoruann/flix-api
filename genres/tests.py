from django.test import TestCase

from .models import Genre


class GenreTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(name="Teste 1")
        Genre.objects.create(name="Teste 2")

    def test_objeto_ativo(self):
        ativo = Genre.objects.get(name="Teste 1")
        self.assertEqual(ativo.name, "Teste 1")
