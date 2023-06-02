"""
Tuplas (tuple)

Existem são bastantes parecidas com listas.
Existem basicamente duas diferenças básicas.
1 - Tuplas são representadas por parênteses ()
print(type(()))
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela nao muda. Toda
operação em uma tupla gera uma nova tupla

# CUIDADO 01: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))
(1, 2, 3, 4, 5, 6)
<class 'tuple'>

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))
(1, 2, 3, 4, 5, 6)
<class 'tuple'>

# Cuidado 02: Tupla com 1 elemento
tupla3 = (4) # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))
# R: 4
# R: <class 'int'>

tupla4 = (4,)  # Isso é uma tupla!
print(tupla4)
print(type(tupla4))
# R: (4,)
# R: <class 'tuple'>

tupla5 = 5,
print(tupla5)
print(type(tupla5))
# R: (5,)
# R: <class 'tuple'>

# CONCLUSÃO: Pode-ser concluir que tuplas são definidas pela vírgula e não pelo parênteses
(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Pode-se gerar uma tupla dinamicamente com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tuplas
tupla = ('Joao', 'Ambrosio')
nome, sobrenome = tupla
print(nome)
print(sobrenome)

# Métdos para: adição e remoção de elementos nas tuplas não existem, dado o fato delas serem imutáveis.
# Soma*, valor máximo*, valor minimo* e tamanho
# Se os valores forem todos inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)
print(tupla1+tupla2) # Tuplas são imutáveis, mas podemos sobrescrever os valores
print(tupla1)
print(tupla2)

# Verificar se determinado elemento está contido na tupla
tupla1 = (1, 2, 3, 4)
tupla2 = (4, 5, 6)
x = int(input("digite: "))
print((x in tupla1) and (x in tupla2))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas, sempre que não devemos motificar os dados contidos em uma coleçao
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos qual mes índice ta na tupla
x = input('mes:')
print(meses.index(x.title()))

# Porque utilizar tuplas
# Tuplas são mais rapidas que listas
# Tuplas deixam seu código mais seguro, porque trabalhar com elementos imutaveis trás segurança ao código.

# Copiando uma tupla para outra
"""
tupla = (1, 2, 3)
print(tupla)

nova = tupla

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)

from collections import namedtuple
meses = namedtuple('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio')
print(meses)
print(meses[1])
