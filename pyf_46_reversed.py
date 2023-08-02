"""
Reversed - integrated function

OBS: Não confunda com a função reverse(), de listas.
A função reverse() funciona somente em listas, já a reversed() com qualquer iterável.

Sua função é inverter o iterável

A função reversed() retorna um iterável chamado <class 'list_reverseiterator'>

# Exemplos

lista = [1, 2, 3, 4, 5, 1, 3]
res = reversed(lista)

print(res) # R: <list_reverseiterator object at 0x000001A465919D20>
print(type(res)) # R: <class 'list_reverseiterator'>

# Lista
print(list(reversed(lista))) # R: [3, 1, 5, 4, 3, 2, 1]
# Tupla
print(tuple(reversed(lista))) # R: [3, 1, 5, 4, 3, 2, 1]
# Conjunto
print(set(reversed(lista))) # R: {1, 2, 3, 4, 5}
# Set não veio invertido, porque em conjunto não é guardado a ordem e nem repete valor!!


"""
# Pode-se iterar sobre o reversed
for letra in reversed('Joao Ambrosio'):
    print(letra, end='') # R: oisorbmA oaoJ

print('\n')
print(''.join(list(reversed('Joao Ambrosio'))))
print(''.join(list('Joao Ambrosio')))

# De forma mais facil, com slice de strings
print('Joao Ambrosio'[::-1])

# pode ser utilizado para loop reverso
for n in reversed(range(10)):
    print(n)
print('\n')
for n in range(9, -1, -1):
    print(n)
