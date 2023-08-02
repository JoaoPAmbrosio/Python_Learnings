"""
Trabalhando com Módulos Builtin (módulos integrados que já vem instalados no Python)
________________________
|Python|Modulos builtin|
-----------------------

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

from random import randint as rdi

print(rdi(5, 16))

from random import randint as redi, random as rdm
from random import randint as rdi, random as rdm, shuffle as shu

# Pode-se importar todas as funções de um módulos utilizando o *

from random import *

print(random())

# import random - Esta importando tudo da mesma forma, mas o uso é diferente.

import random
print(random.random())



"""

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(5, 11))
lista1 = ['1', '2', '3', '4', '5']
shuffle(lista1)
print(lista1)
print(choice(['pedra', 'papel', 'tesoura']))



