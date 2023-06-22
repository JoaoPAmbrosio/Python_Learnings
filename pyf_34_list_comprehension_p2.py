"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

"""
# Exemplo 01
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares) # R: [2, 4, 6]
print(impares) # R: [1, 3, 5]

# Refatorar
# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares) # R: [2, 4, 6]
print(impares) # R: [1, 3, 5]

# Exemplo 02

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res) # R: [0.5, 4, 1.5, 8, 2.5, 12]


