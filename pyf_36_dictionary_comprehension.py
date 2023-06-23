"""
Dictionary Comprehension

Se deseja-se criar uma lista:
lista = [1, 2, 3, 4]
Se deseja-se criar uma tupla:
tupla = (1, 2, 3, 4)
Se deseja-se criar um set (conjunto):
set = {1, 2, 3, 4}
Se deseja-se criar um dicionário:
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd':4}

# Sintaxe
{chave:valor for valor in iterável}

# Exemplo 01
numeros = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado) # R: {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}

numeros = [1, 2, 3, 4, 5, 1, 2] # Como em dicionario nao há a repeticao de chave, o 1 e 2 nao se repetem
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados) # R: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
print(len(chaves))

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
"""
# Exemplo com lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
