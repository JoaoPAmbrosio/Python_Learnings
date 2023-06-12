"""
Módulo Collections - Named Tuple
https://docs.python.org/3/library/collections.html#collections.namedtuple
# Recap Tupla
tupla = (1, 2, 3)
print(tupla[1])

named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.

# Import
from collections import namedtuple

# Precisa-se definir o nome e parâmetros.
# Forma 01 - Declaração Named Tuple
cachorro1 = namedtuple('dog', 'idade raça nome')
# Forma 02 - Declaração Named Tuple
cachorro = namedtuple('dog', 'idade, raca, nome')
"""
# Import
from collections import namedtuple

# Forma 03 - Declaração Named Tuple
cachorro = namedtuple('info_dos_dog', ['idade', 'raca', 'nome']) # Mais interessante de usar
print(cachorro)
print('espaco')
# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados
# Forma 01
print(ray[0]) # idade
print(ray[1]) # raca
print(ray[2]) # nome

# Forma 02
print(ray.idade) # idade
print(ray.raca) # raca
print(ray.nome) # nome
x= 'Ray'
print(ray.index(x))
print(ray.count(x))
