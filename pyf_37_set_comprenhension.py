"""
Set comprenhension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

# Exemplo
numeros = {num for num in range(1, 7)}
print(numeros) # R: {1, 2, 3, 4, 5, 6}

# Outro Exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros) # R: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25} Sem ordem

# DESAFIO! Fazer alteração na estrutura para gerar um dicionario ao inves de ser
numeros = {x:x ** 2 for x in range(10)}
print(numeros) # R: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

for letra in range(0, len(nome)):
    print(nome[letra])
"""
nome = 'Joao Ambrosio'
res = {letra: letra for letra in nome}
print(res)
"""
desafio: colocar em numero
letras = {[n for n in range(0, len(nome))], letra in nome.items()}
print(letras)
"""
