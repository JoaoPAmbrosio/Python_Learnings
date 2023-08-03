"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # É uma função (logar) dentro de outra
        print(f'Voce está chamando: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar
@ver_log
def soma(a, b):
    # Soma dois números
    return a + b

print(soma(10, 30))

print(soma.__name__) # R:(puxando da decorator) logar
print(soma.__doc__) # R:(puxando da decorator) É uma função (logar) dentro de outra

"""

# Resolução do problema
from functools import wraps
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """É uma função (logar) dentro de outra"""
        print(f'Voce está chamando: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar
@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b
print(soma(10, 30))
print(soma.__name__) # R:soma
print(soma.__doc__) # R:Soma dois números



