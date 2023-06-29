"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar
esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se voce realmente precisa dela. Em todo caso, 99% das vezes um loop for é
mais legível.

para entender o reduce()

# Colecao de dados:
dados = [a1, a2, a3, ..., an]

# Função que recebe dois parametros:


def funcao(x, y):
    return x * y

    
Assim como map() e filter() recebe dois parametros: a função e o iterável
reduce(funcao, dados)
A funcao reduce(), funciona:
   Passo 1: res1 = f(a1, a2) # Aplica a funçao nos dois primeiros elementos da coleção e guarda o resultado.
   Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado passo1 mais o terceiro elemento e guarda o res.

   Isso é repetido até o final.
   Passo 3: res3 = f(res3, a4)
   .
   .
   .
   Passo n: resn = f(resm, an)
Ou seja, em cada passo ela aplica a funçao passando como primeiro argumento o resultado aplicado anterior. No final,
reduce() erá retornar o resultado final.

Alternativamente, poderíamos ver a funcao reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""
# Forma 01
res = 2*3*4*5*7*11*13*17*19*23*29
print(res) # R: 25878772920

# Forma 02
from functools import reduce
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
# Para utilizar o reduce() precisa-se de uma função que receba dois parâmetros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res) # R: 25878772920

# Forma 03
res = 1
for n in dados:
    res = res*n
print(res) # R: 25878772920
