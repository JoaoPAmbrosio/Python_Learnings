"""
Any e All

All() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exemplo all()

# print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros? False
# print(all([1, 2, 3, 4])) # Todos os números são verdadeiros? True
# print(all([])) # Todos os números são verdadeiros? True
# print(all((1, 2, 3, 4))) # Todos os números são verdadeiros? True
# print(all({1, 2, 3, 4})) # Todos os números são verdadeiros? True
# print(all('Geek')) # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina']
print(all(n[0] == 'C' for n in nomes)) # R: True

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou'])) # R: ['e', 'i', 'o'] , True
print(all([letra for letra in 'eio' if letra in 'fk'])) # R: [] , True (apenas em ALL)

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False


"""
print(any([0, 1, 2, 3, 4])) # R: True
print(any([0, False, {}, (), []])) # R: False
nomes = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina']
print(any([n[0].lower() == 'c' for n in nomes])) # R: False
