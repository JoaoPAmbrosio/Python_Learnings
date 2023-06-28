"""
Filter  - integrated function

filter() -> Servem para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
dados.sort()
print(dados)
# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)
print(media)
# OBS: Assim como a funcao map(), a filter() recebe dois parametros, sendo um funcao e um iterável

res = filter(lambda x: x > media, dados)
print(type(res)) # R: <class 'filter'> -> Filter object
print(list(res)) # R: [2.7, 4.1, 4.3]
print(list(res)) # R: [] -> Após ser utilizado os dados de filter() eles são excluidos, assim como map

# Remoçao da dados faltantes

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
'''
# Duas formas
res = filter(lambda pais: pais != '', paises) # Tipo None é o tipo vazio, faz com que vazios sejam eliminados
print(list(res))
res = filter(lambda pais: len(pais) > 0, paises) # Tipo None é o tipo vazio, faz com que vazios sejam eliminados
print(list(res))
'''
# Forma com None
res = filter(None, paises) # Tipo None é o tipo vazio, faz com que vazios sejam eliminados
print(list(res))

# Diferença entre map() e filter() é:
# map() -> Recebe dois parametros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento
# do iterável.
# filter() -> Recebe dois parametros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de
# acordo com a função.


# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

# Filtrar os usuários que estao inativos no Twitter
print(len(usuarios[1]['tweets']) == 0) # Aprendendo a logica

# Forma 01
# inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
# print(inativos)

# Forma 02 - Sem o not é retirado todos os vazios!!
inativos = list(filter(lambda u: not u['tweets'], usuarios)) # [] é igual a False. not False é igual a True
print(inativos)
# OBS: Lista vazia transformada em Boolean (bool) é False. Qualquer elemento em bool é True
a = bool()
print(a) # R: False
b = bool('a')
print(b) # R: True


"""
nomes = ['Vanessa', 'Ana', 'Maria']

# Deve-se criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

print(list(map(lambda nome: f'Sua instrutora é {nome}', nomes)))
# R: ['Sua instrutora é Vanessa', 'Sua instrutora é Ana', 'Sua instrutora é Maria']
print(list(filter(lambda nome: len(nome) < 5, nomes)))
# R: ['Ana']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista) # R:['Sua instrutora é Ana']
