"""
Min e Max - integrated function

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elemento.

# Exemplos

list = [1, 8, 4, 99, 34, 129]
print(max(list)) # R: 129

tuple = (1, 8, 4, 99, 34, 129)
print(max(tuple)) # R: 129

set = {1, 8, 4, 99, 34, 129}
print(max(set)) # R: 129

dicionary = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionary.values())) # R: 129

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))
print(max(4, 67, 54)) # R: 67
print(max('a', 'ab', 'abc')) # R: abc
print(max('a', 'b', 'c', 'g')) # R: g
print(max(3.145, 5.324)) # R: 5.324

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

# Exemplos

list = [1, 8, 4, 99, 34, 129]
print(min(list)) # R: 1

tuple = (1, 8, 4, 99, 34, 129)
print(min(tuple)) # R: 1

set = {1, 8, 4, 99, 34, 129}
print(min(set)) # R: 1

dicionary = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionary.values())) # R: 1

# Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))
print(min(4, 67, 54)) # R: 4
print(min('a', 'ab', 'abc')) # R: a
print(min('a', 'b', 'c', 'g')) # R: a
print(min(3.145, 5.324)) # R: 3.145

# Outros exemplos
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander', 'Sy']
print(max(nomes)) # R:Tim, ordem alfabetica
print(min(nomes)) # R:Arya
print(max(nomes, key=lambda x: len(x))) # R: Ollivander
print(min(nomes, key=lambda x: len(x))) # R: Sy, numero de caracteres

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]
print(max(musicas, key=lambda m: m["tocou"]))
print(min(musicas, key=lambda m: m["tocou"]))

# Imprimindo somente o titulo
print(max(musicas, key=lambda m: m["tocou"])["titulo"])
print(min(musicas, key=lambda m: m["tocou"])["titulo"])

# Sem max, min ou lambda
"""
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

i = []
m = 0
for musica in musicas:
    if musica["tocou"] > m:
        m = musica["tocou"]
        i = musica
print(i)
for musica in musicas:
    if musica["tocou"] < m:
        m = musica["tocou"]
        i = musica
print(i)
# print([n for x in musicas if n["tocou"] > x["tocou"]])
