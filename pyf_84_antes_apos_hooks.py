"""
------
hooks - são os testes em si, a execução dos testes
------

setup() -> é executado antes de cada método de teste. É util para criarmos instancias de objetos e outros dados;

tearDown() -> é executado ao final de cada método de teste. É util para excluie dados ou fechar conexoes com banco de
dados.

"""
import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self) -> None:
        # Configuracoes do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_terceiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def tearDown(self) -> None:
        # Configuração do tearDown
        pass
