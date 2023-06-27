"""
Map  - integrated function

Com map, fazemos mapeamento de valores para função.


import math

def area(r):
    # Calcula a area de um circulo com raio 'r'.
    return math.pi * (r ** 2)

# print(area(2)) # R: 12.566370614359172
# print(area(5.3)) # R: 88.24733763933729

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma 01 comum
areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# Forma 02 list comprenhension
areas = [area(r) for r in raios]
print(areas)

# Forma 03 map
# Map é uma função que receve dois parâmetros: O primeiro a funçao, o segundo um iterável. Retorna um Map Object

areas = map(area, raios)

# print(areas) # R: <map object at 0x000002379F05BA90>
# print(type(areas)) # R: <class 'map'>
print(list(areas)) # R: [12.566370614359172, 78.5398163397, ..... , ]
# print(tuple(areas)) # R:()
# OBS: Após utilizar a função map() depois da primeira utilizacao do resultado, ele zera.

# Forma 04 Map com Lambda
x = map(lambda r: math.pi * (r ** 2), raios)
print(list(x)) # R: [12.566370614359172, 78.5398163397, ..... , ]
print(list(x)) # R: []
print(list(map(lambda r: math.pi * (r ** 2), raios))) # R: [12.566370614359172, 78.5398163397, ..... , ]

# Para fixar - Map

# Temos dados iteráveis:

# dados: a1, a2, ..., an

# Temos uma funçao:

# Função: f(x)

# Utilizamos a função map(f , dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an)


"""
# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27),
           ('Nova York', 28), ('Londres', 22)]

print(cidades)
print(cidades[0][1])
# f = 9/5 * c + 32
# Lambda
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

# Arredondamento?

