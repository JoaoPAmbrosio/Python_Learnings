"""
Introdução ao módulo Unittest

Unittest -> Testes unitários

O que são testes unitários?
Testes é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funcoes, metodos, classes, modulos, etc.

OBS: Teste unitario não é especifico da linguagem Python.

Para criar os testes, cria-se classes que herdam de unittest. TestCase e a partir de entao ganha-se todos os'assertions'
presentes no módulo.

Para rodar os testes, utiliza-se unittest.main()

TestCase -> Casos de testes para a unidade
http://docs.python.org/3/library/unittest.html
https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

# Conhecendo os assertions

Method                        Checks that
assertEqual(a, b)             a == b
assertNotEqual(a, b)          a != b
assertTrue(x)                 bool(x) is True
assertFalse(x)                bool(x) is False
assertIs(a, b)                a is b
assertIsNot(a, b)             a is not b
assertIsNone(x)               x is None
assertIsNotNone(x)            x is not None
assertIn(a, b)                a in b
assertNotIn(a, b)             a not in b
assertIsInstance(a, b)        isinstance(a, b)
assertNotIsInstance(a, b)     not isinstance(a, b)

Por convenção, todos os testes em um test case, devem ter seu nome iniciado com test_

# 01 - Para executar os testes com unittest
python nome_do_modulo.py

# 02 - Para executar os testes com unittest no modo verbose
python nome_do_modulo.py -v

# Docstrings nos testes
Pode ser acrescentado (e é recomendado) docstrings nos testes.


Unittest - Antes e após hooks


"""




