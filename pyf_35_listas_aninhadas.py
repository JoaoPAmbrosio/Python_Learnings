"""
Listas Aninhadas (Nested lists)
- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Limitações de C/Java -> Tamanho e tipo de dado

Em Python se tem as listas
numeros = [1, 'b', 3.234, True, 5]


listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)
print(type(listas))

# Como se faz para acessar os dados?
print(listas[0][1]) # Linha 0, coluna 1

# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)


# List Comprenhensions

[[print(valor) for valor in lista] for lista in listas]
"""
# Outros exemplos
# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])





