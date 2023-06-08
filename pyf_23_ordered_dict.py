"""
Módulo Collections: Ordered Dict
https://docs.python.org/3/library/collections.html#collections.OrderedDict
OrderedDict -> É um dicionário, que garante a ordem de inserção dos elementos


dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
# Em um dicionário, a ordem de inserçao dos elementos não é garantida

# Fazendo o import
from collections import OrderedDict
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
# Nesse momento a ordem é garantida pelo OrderedDict, alem de ganho de performance.



"""
# Entendendo a diferença entre Dict e OrderedDict

# Dicionários comuns
dict1 ={'a': 1, 'b': 2}
dict2 ={'b': 2, 'a': 1}
print(dict1 == dict2) # True -> Uma vez que a ordem os elementos não importa para o diconário

# Ordered Dict
from collections import OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2) # False -> Já que a ordem dos elementos importa para o OrderedDict


