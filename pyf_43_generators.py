"""
Generator Expression - integrated function

Sabe-se:
- List comprehensions
- Dictionary Comprehensions
- Set comprehensions
# Foi usado
nomes = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina']
print(any([n[0].lower() == 'c' for n in nomes]))

# Poderia ter sido utilizado Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina']
print(tuple(n[0].lower() == 'c' for n in nomes))

# List comprehensions
res = [n[0].lower() == 'c' for n in nomes]
print(type(res)) # R: <class 'list'>
print(res)

# Generator
res = (n[0].lower() == 'c' for n in nomes)
print(type(res)) # R: <class 'generator'>
print(res)

# Generator ocupa menos recurso em memória. Melhor em performance. É sempre mais performatico quando comparado
com qualquer outro


# A função/utilizade de getsizeof() é retornar a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Joao')) # R: 53
print(getsizeof('Ambrosio')) # R: 57
print(getsizeof(9)) # R: 28
print(getsizeof(9165416516531)) # R: 32
print(getsizeof(True)) # R: 28

"""
from sys import getsizeof

# Gerando lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
# Gerando lista de números com set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
# Gerando lista de números com Dicionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
# Gerando lista de números com Dicionary Comprehension
gen = (x * 10 for x in range(1000))

print(f'List Comprehension: {list_comp} bytes') # R:8856 bytes
print(f'Set Comprehension: {set_comp} bytes') # R: 32984 bytes
print(f'Dictionary Comprehension: {dic_comp} bytes') # R: 36952 bytes
print(f'Generator Expression: {getsizeof(gen)} bytes') # R: 208 bytes

# Iterando no Generation Expression
print(gen) # R: <generator object <genexpr> at 0x000001BEE996FED0>
print(type(gen)) # R: <class 'generator'>

# print([n for n in gen]) # R: [0, 10, 20, 30, 40,..., 9980, 9990]
for n in gen:
    print(n)
# R: 0
# R: 10
# R: 20
# R: ...
# R: 9990
