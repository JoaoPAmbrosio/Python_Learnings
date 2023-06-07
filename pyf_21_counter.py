"""
Módulo Collections - Counter
https://docs.python.org/3/library/collections.html#collections.Counter
Collections -> High-performance Container Datatypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chava o elemeto da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento

# Realizando o import
from collections import Counter
# Pode ser utilizado qualquer iterável
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
# Utilizando o Counter
# Exemplo 01
res = Counter(lista)
print(type(res)) # <class 'collections.Counter'>
print(res) # Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 02
from collections import Counter
print(Counter('Joao Ambrosio')) # Counter({'o': 4, 'J': 1, 'a': 1, ' ': 1, 'A': 1, 'm': 1, 'b': 1, 'r': 1, 's': 1, 'i': 1})

"""
# Exemplo 03
from collections import Counter

texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido 
na internet sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável
​​, que todos possam editar e melhorar. O projeto é definido pelos princípios fundadores e o 
conteúdo é disponibilizado sob a licença Creative Commons BY-SA e pode ser reutilizado sob a mesma licença,
 desde que respeitando os termos de uso."""

palavras = texto.split()
print(palavras) # ['A', 'Wikipédia', 'é', 'um', 'projeto', 'de', 'enciclopédia', ..., 'de', 'uso.']

res = Counter(palavras)
print(res) # Counter({'e': 5, 'é': 3, 'sob': 3, 'um': 2, 'projeto': 2, 'de': 2, 'o': 2, ..., 'uso.': 1})

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5)) # [('e', 5), ('é', 3), ('sob', 3), ('um', 2), ('projeto', 2)]

