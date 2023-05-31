"""
Ranges

- Precisamos conhecer o loop para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 01
range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma 01
for num in range(11):
    print(num)

# Forma 02
range(valor_de_parada, valor_de_parada)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Exemplo Forma 02
for num in range(1, 11):
    print(num)

# Forma 03
range(valor_de_parada, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuario)

# Exemplo Forma 03
for num in range(1, 11, 2):
    print(num)

# Forma 04 (inversa)
range(valor_final, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e decremento especificado pelo usuario)

# Exemplo Forma 04
for num in range(10, 0, -1):
    print(num)
"""

