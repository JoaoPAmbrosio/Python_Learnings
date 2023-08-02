"""
Len, Abs, Sum, Round - integrated function

# Len
len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável

print(len('Joao Ambrosio')) # R:13
print(len([1, 2, 3, 4, 5])) # R:5
print(len((1, 2, 3, 4, 5))) # R:5
print(len({1, 2, 3, 4, 5})) # R:5
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})) # R:5
print(len(range(6))) # R:6

# Dentro da máquina, quando utilizado a função len() o Python faz o seguinte:

# Dender len
print('Joao Ambrosio'.__len__()) # R: 13


# Abs
abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplos Abs
print(abs(-5)) # R:5
print(abs(5)) # R:5
print(abs(3.14)) # R:3.14
print(abs(-3.14)) # R:3.14
print(abs('Joao')) # R: TypeError: bad operand type for abs(): 'str' ... Não opera string!

# Sum
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elementos,
incluindo o valor incial.
# OBS: O valor inicial default = 0

print(sum([1, 2, 3, 4, 5])) # R:15
print(sum((1, 2, 3, 4, 5))) # R:15
print(sum({1, 2, 3, 4, 5})) # R:15
print(sum([(sum((1, 2, 3))), 4], 5)) # R: 15
print(sum(range(6))) # R:15
print(sum([1, 2] , [3, 4] , [5])) # R:TypeError: sum() takes at most 2 arguments (3 given)
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})) # R:TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values())) # R:15
print(sum('Joao Ambrosio')) # R: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Round
round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a decisão não for
informada retorna o inteiro mais proximo da entrada.
"""
print(round(10.2)) # R:10
print(round(10.49)) # R:10
print(round(10.50)) # R:10
print(round(10.51)) # R:11
print(round(1.21212121, 2)) # R:1.21
print(round(1.2151, 2)) # R:1.22
print(round(1.215178, 3)) # 1.215
