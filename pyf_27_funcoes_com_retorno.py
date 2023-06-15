"""
Funções com retorno

# Exemplos de funções com retornos e sem retornos:
numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}') # R: 3
ret_pr = print(numeros)
print(f'Retorno de print: {ret_pr}') # R: None

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None
OBS: Funções Python que retornam valores, devem retornar estes valores com a palabra reservada return
OBS: Não é necessário necessariamente criar uma variável para receber o retorno
de uma função. Pode-se o passar a execução da funçao para outras funções.

# Exemplo função

def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7() # R: 49
print(f'Retorno de {ret}') # R: Retorno de None

# Refatore (reescrever/redefinir/Modificar codigo para trabalhar melhor) esta função
# para que ela retorne o valor


def quadrado_de_7():
    return 7 * 7


# Foi criado uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno de {ret + 1}') # R: Retorno de 50

# Sem criar a variavel
print(f'Retorno: {quadrado_de_7() + 1}') # R: Retorno: 50

# Refatorando a primeira função


def diz_oi():
    return 'oi '


alguem = 'Joao'
print(diz_oi() + alguem) # R: oi Joao

# OBS: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Pode-se ter, em uma função, diferentes returns;
3 - Pode-se, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

# Exemplos 01 - Após o return, nada é executado!!


def diz_oi():
    print('Estou sendo executado antes o retorno... ') # R: Estou sendo executado antes o retorno...
    return 'Oi '
    print('Estou sendo executado após o retorno... ') # R: (Sem resposta, não lido pelo programa)


print(diz_oi()) # R: Oi

# Exemplo 02 - Diferentes returns


def nova_funcao():
    variavel = False
    if variavel: # Podemos deixar sem o True, ta subtendido.
        return 4
    elif variavel is None: # PEP8: Usar o 'is', no lugar de '==', por mais que os dois rodam
        return 3.2
    return 'b' # String. Não precisa colocar o Else, porque é desnecessário


print(nova_funcao())

# Exemplo 03 - Retornar qualquer tipo de dado e até mesmo múltiplos valores;


def outra_funcao():
    return 2, 3, 4, 5 # Esta sendo gerado uma Tupla, por causa da virgula. A forma como esta sendo solicitado o return


print(outra_funcao()) # Forma uma tupla = (2, 3, 4, 5)
# outra_funcao() = num1, num2, num3, num4 | Não funciona assim!
num1, num2, num3, num4 = outra_funcao() # Isso é um DESEMPACOTAMENTO!
print(num1, num2, num3, num4) # R: 2 3 4 5
print(num3, num4, num1, num2) # R: 4 5 2 3, que mostra que imprimi em ordem

# Exercicio: Criar uma função para jogar moeda

from random import random
# Existe um pacote 'random' dentro da biblioteca Python e esta sendo aprendido a funçao 'random' dentro dele


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1. É dito 'pseudo'-randômica pela possibilidade de repetição
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
# PROBLEMA! Não consegui importar esse arquivo de biblioteca para importar a função, no terminal por causa
# do numero que antecede o nome da biblioteca "27-"funcoes_com_retorno. Quando retirado, rodou
"""
# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação necessária


def eh_impar():
    numero = 61
    if numero % 2 != 0:
        return True
    return False # Evite colocar 'else' caso não tenha necessidade


print(eh_impar())
