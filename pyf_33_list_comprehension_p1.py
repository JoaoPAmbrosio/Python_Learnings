"""
List comprehension

- Utilizando o List Comprehension pode-se gerar novas listas com dados processados a partir de outro iterável.

# Sentaxe da List Comprenhension

[ dado for dado in iterável ]
[ valor for valor in iterável ]

# Exemplos
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
riu = numeros * 10
print(res) # R:[10, 20, 30, 40, 50]
print(riu) # R:[1, 2, 3, 4, 5, 1, ..... , 3, 4, 5]

Para entender melhor o que está acontecendo deve-se dividir a expressao em das duas partes:
- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)


# List comprenhension versos Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# List comprenhensions
numeros_dobrados = [numero * 2 for numero in numeros]
print(numeros_dobrados)

"""

# Outros exemplos
# Exemplo 01
nome = 'Joao Ambrosio'
print([letra for letra in nome]) # R: ['J', 'o', 'a', 'o', ' ', 'A', 'm', 'b', 'r', 'o', 's', 'i', 'o']

# Exemplo 02
print([numero * 3 for numero in range(1, 10)]) # R: [3, 6, 9, 12, 15, 18, 21, 24, 27]

# Exemplo 03
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]]) # R: [False, False, False, True, True, True]

# Exemplo 04
# Transformandom, em vez de trabalhar com inteiro, trabalhando com strings
print([str(numero) for numero in [1, 2, 3, 4, 5]]) # ['1', '2', '3', '4', '5']


