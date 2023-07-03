"""
Sorted - integrated function

OBS: Não confundi com função sort() de Listas. O sort() só funciona em Listas

Pode-se utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.
OBS: O sorted sempre retorna uma lista com os elementos iteráveis ordenados

# Exemplo

numeros = (6, 1, 8, 2)

print(sorted(numeros)) # Ordenar do menor para o maior, retornando em lista. R: [1, 2, 6, 8]
print(numeros) # R: (6, 1, 8, 2)

numeros = (6, 1, 8, 2)

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor, em lista R:[8, 6, 2, 1]

# Pode-se utilizar o sorted() para coisas mais complexas
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "vou sair hoje"]},
    {"username": "gal", "tweets": []},
]
print(usuarios[0]["username"])
# Ordenar pelo nome de usuário - Ordem Alfabética
# key é o parametro. Para cada usuario toda a da lista de usuario , recebe o usuario"u" x "username" e ordena
print(sorted(usuarios, key=lambda u: u["username"], reverse=True))

# Ordenar pelo numero de tweets. Ordem decrescente com o reverse
print(sorted(usuarios, key=lambda u: len(u["tweets"]), reverse=True))

"""
# Exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]
print(musicas[0]["tocou"])
print(sorted(musicas, key=lambda m: m["tocou"], reverse=True))


