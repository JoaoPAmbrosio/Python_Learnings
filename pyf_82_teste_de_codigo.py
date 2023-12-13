"""
Testes automatizados

- Reduzir bugs (problemas) no código existente;
- Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
- Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
- Testes garantem que a refatoração que costuma-se a fazer não tragam novos bugs (problemas);

TDD - Test Driven Development ( Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:
    - É escrito o teste primeiro;
    - Entao é escrito o código mínimo suficiente para fazer o testes passar (ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que é seguido pelos desenvolvedores conhecidos como:
    - Red; (Escrever um teste que vai falhar e voce vai saber que vai falhar por falta de codigo)
    - Green; (Escreve o codigo mínimo para se funcionar )
    - Refactor; (Ajusta o codigo para que cumpra a atividade prevista)

Assertions (Afirmações/Checagens/Questionamentos)

Em Python utiliza-se a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.

Utiliza-se o 'assert' em uma expressão que se quer chegar se é validada ou nã. Se a expressão for verdadeira, retorna
Nohe e caso seja Falsa, levanta um erro do tipo AssertionError.

OBS: Não se pode especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada
OBS: A palavra 'assert' pode ser utilizada em qualquer funcao ou código nosso... nao precisa ser exclusivamente nos
testes.

ALERTA: Cuidado ao utilizar 'assert'
Um programa Python executado com o parametro -O, nenhum assertion será validado. Ou seja, perde todas as validações.

Abrindo o programa com o parâmetro:
python -O pyf_82_teste_de_codigo.py
Dessa forma os assertions nao funcionam

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos numeros precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(2, 4) # R: 6
# ret = soma_numeros_positivos(-2, 4) # R: AssertionError: Ambos numeros precisam ser positivos
print(ret)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'batata frita',
        'cachorro quente',
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

comida = input('informe a comida: ')
print(comer_fast_food(comida))

# ALERTA: Cuidado ao utilizar 'assert'
'''def faca_algo_ruim(usuario):
    assert usuario.eh_admin, 'Somente administradores tem permissão'
    destroi_todo_o_sistema()
    return 'Adeus'
'''


Doctests

São testes que são colocados na docstring das funções/métodos Python.
Para rodar um test do doctest
python -m doctest -v nome_do_modulo.py

def soma(a, b):
    (tres aspas)soma os números a e b

    # >>> soma(1, 2)
    3
    # >>> soma(2, 2)
    5
    (tres aspas)
    return a + b
print(soma(3, 4))

python -m doctest -v pyf_82_teste_de_codigo.py
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    pyf_82_teste_de_codigo
1 items passed all tests:
   1 tests in pyf_82_teste_de_codigo.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

Com um teste errado!

Trying:
    soma(1, 2)
Expecting:
    3
ok
Trying:
    soma(2, 2)
Expecting:
    5
**********************************************************************
File "C:/Users/joaop/PycharmProjects/guppe/pyf_82_teste_de_codigo.py", line 95, in pyf_82_teste_de_codigo.soma
Failed example:
    soma(2, 2)
Expected:
    5
Got:
    4
1 items had no tests:
    pyf_82_teste_de_codigo
**********************************************************************
1 items had failures:
   1 of   2 in pyf_82_teste_de_codigo.soma
2 tests in 2 items.
1 passed and 1 failed.
***Test Failed*** 1 failures.


def duplicar(valor):
    '''Duplica os valores em uma lista
    # >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    # >>> duplicar([])
    []
    # >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']
    # >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    '''
    return [2 * elemento for elemento in valor]


# Erro inpesperado
def fala_oi():
    '''Fala oi

    # >>> fala_oi()
    'oi'
    '''
    return "oi"

Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.


"""

# Caso estranho

def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True


