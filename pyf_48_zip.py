"""
Zip - integrated function

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.

# Exemplo

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1) # R: <zip object at 0x0000026570C3FA80>
print(type(zip1)) # R: <class 'zip'>

# Sempre pode-se gerar uma Lista, Tupla, Dicionário
print(list(zip(lista1, lista2))) # R: [(1, 4), (2, 5), (3, 6)]
print(tuple(zip(lista1, lista2))) # R: ((1, 4), (2, 5), (3, 6))
print(set(zip(lista1, lista2))) # R: {(2, 5), (1, 4), (3, 6)}
print(dict(zip(lista1, lista2))) # R: {1: 4, 2: 5, 3: 6}

lista3 = [7, 8, 9, 10, 11]
print(list(zip(lista1, lista2, lista3))) # R: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip(lista2, lista3, lista1))) # R: [(4, 7, 1), (5, 8, 2), (6, 9, 3)]
# OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando com
# iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar, independente da ordem.

# Pode-se utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario) # R: [(1, 6, 'a'), (2, 7, 'b'), (3, 8, 'c'), (4, 9, 'd'), (5, 10, 'e')]
zt = zip(tupla, lista, dicionario.values()) # R:[(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados))) # R: [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

print(list(zip(alunos, prova1, prova2))) # R: [('maria', 80, 98), ('pedro', 91, 89), ('carla', 78, 53)]
for dado in zip(alunos, prova1, prova2):
    print(dado)
# R: ('maria', 80, 98)
# R: ('pedro', 91, 89)
# R: ('carla', 78, 53)
print({dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)})
# R: {'maria': 98, 'pedro': 91, 'carla': 78}

"""
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

# Pode ser utilizado o map
print(dict(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))))
