"""
Debugando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# OBS: A utilização do print() para debugar código é uma prática ruim
def dividir(a, b):
    print(a, b)
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Voce digitou valor errado! {err}'
print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger. Em Python, pode-se fazer isso em
# diferentes IDEs, como PyCharm ou utilizando o PDB - Python Debugger.

# Exemplo com PyCharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Voce digitou valor errado! {err}'
print(dividir(4, 0))

# Exemplo 01, com o PDB - Python Debugger
# Para utilizar o Python Debugger, precisa-se* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l - para listar onde esta no código
# n - próxima linha
# p - imprimi a variável
# c - continua a execução/finaliza o debugging

import pdb
nome = 'angelina'
sobrenome = 'jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo.title() + ' faz o curso '.lower() + curso.lower()
print(final)

# Exemplo 02, com o PDB - Python Debugger
# Para utilizar o Python Debugger, precisa-se* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l -(list) - para listar onde esta no código
# n (next) - próxima linha
# p (print)- imprimi a variável
# c (continue)- continua a execução/finaliza o debugging

nome = 'angelina'
sobrenome = 'jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo.title() + ' faz o curso '.lower() + curso.lower()
print(final)

# Porque utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costuma-se realizar todos os imports de bibliotecas no início do
# arquivo. Por isso, ao invés de colocar o import do pdb no início do arquivos, coloca-se somente onde vai debuggar
# e ao finalizar faz-se a remoção.

# Exemplo 03, com o PDB com breakpoint() - Python Debugger
# Para utilizar o Python Debugger, precisa-se* importar a biblioteca pdb e então utilizar a função set_trace()

# * A partir do Python 3.7, não é mais necessário importar a bilbioteca pdb, pois o comando de debug foi incorporada
# como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l -(list) - para listar onde esta no código
# n (next) - próxima linha
# p (print)- imprimi a variável
# c (continue)- continua a execução/finaliza o debugging

nome = 'angelina'
sobrenome = 'jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo.title() + ' faz o curso '.lower() + curso.lower()
print(final)


"""
# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c
print(soma(1, 2, 3, 4))
# Como os nomes das variáveis são os mesmos dos comandos do pdb, deve-se utilizar o comando p para imprimir as
# variáveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes não representativos nas variáveis. Sempre optar por nomes significativos.
def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4


