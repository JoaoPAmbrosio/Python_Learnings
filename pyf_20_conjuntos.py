"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, esta sendo feito referencia à Teoria dos Conjuntos
da Matemática.

- Os conjuntos são chamados de Sets.

Da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando se armazena elementos
mas não se importa com a ordenação deles. Quando não precisa se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:
# Forma 01
s = ({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que existe valores repetidos.
print(s) # {1, 2, 3, 4, 5, 6, 7}
print(type(s)) # <class 'set'>
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 02 - Mais comum
s ={1, 2, 3, 4, 5, 5}
print(s) # {1, 2, 3, 4, 5}
print(type(s)) # <class 'set'>

# Pode verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('tem o 3')
else:
    print('Nao tem o 3')

# Quando coloca-se '', "", nos dados
dados = '99, 2, 34, 23, 2, 12, 1, 44, 5, 34'
lista = list(dados)
print(f'Lista: {lista}')
# R: Lista: ['9', '9', ',', ' ', '2', ',', ' ', '3', '4', ',', ' ', '2', '3', ',', ' ', '2', ',', ' ', '1', '2', ',', ' ', '1', ',', ' ', '4', '4', ',', ' ', '5', ',', ' ', '3', '4']
tupla = tuple(dados)
print(f'Tupla: {tupla}')
# R: Tupla: ('9', '9', ',', ' ', '2', ',', ' ', '3', '4', ',', ' ', '2', '3', ',', ' ', '2', ',', ' ', '1', '2', ',', ' ', '1', ',', ' ', '4', '4', ',', ' ', '5', ',', ' ', '3', '4')
dicionario = (dados, 'dict')
print(f'Dicionário: {dicionario}')
# R: Dicionário: ('99, 2, 34, 23, 2, 12, 1, 44, 5, 34', 'dict')
dicciona = dict(dados='dict2')
print(f'Dicciona: {dicciona}')
# R: Dicciona: {'dados': 'dict2'}
conjunto = set(dados)
print(f'Conjunto: {conjunto}')
# R: Conjunto: {',', '1', ' ', '3', '9', '2', '5', '4'}

# Importante lembrar que, além de não ter valores duplicados, não existe ordem
dados = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

# Listas aceitam valores duplicados
lista = list(dados)
# ou lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos.')
# R: Lista: [99, 2, 34, 23, 2, 12, 1, 44, 5, 34] com 10 elementos.

# Tuplas aceitam valores duplicados
tupla = tuple(dados)
# ou tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos.')
# R: Tupla: (99, 2, 34, 23, 2, 12, 1, 44, 5, 34) com 10 elementos.

# Dicionarios nao aceitam chaves duplicadas
dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos.')
# R: Dicionário: {99: 'dict', 2: 'dict', 34: 'dict', 23: 'dict', 12: 'dict', 1: 'dict', 44: 'dict', 5: 'dict'} com 8 elementos.

dicciona = dict(dados='dict2') # errado, nao linka a dados
print(f'Dicciona: {dicciona} com {len(dicciona)} elementos.')
# R: Dicciona: {'dados': 'dict2'} com 1 elementos.

# Conjuntos nao aceitam valores duplicados, ordenação própria
conjunto = set(dados)
# ou conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos.')
# R: Conjunto: {1, 2, 99, 34, 5, 12, 44, 23} com 8 elementos.

# Assim como todo outro conjunto Pyton pode colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.22, 44}
print(s) # R: {'b', 1, 34.22, 44}
print(type(s)) # R: <class 'set'>

# Pode se iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que foi feito um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# É adicionado cada cidade em uma lista Python, já que em uma lista pode-se adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades)) # R: 7
print(len(set(cidades)))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, tem-se:
lista1 = set(cidades)
print(lista1)
print(len(lista1))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4) # duplicidade nao gera erro, simplesmente não é adicionado
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
# Forma 01
s.remove(2) # Não é indice, mas sim valor.
print(s)
# OBS: Caso o valor não seja encontrado, será gerado o erro KeyError

# Forma 02
ret = s.discard(3)
print(s)
# OBS: Caso o valor não seja encontrado, NÃO será gerado erro

# Copiando um conjunto para outro
s = {1, 2, 3}
# Forma 01 - Deep copy
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)
# Forma 02 - Shallow copy
novo = s
print(novo)
novo.add(4)
print(novo)
print(s)

# Remover todos itens de um conjunto
s = {1, 2, 3}
print(s)
s.clear()
print(s)


# MÉTODOS MATEMÁTICOS DE CONJUNTOS
# Imagine que tem-se dois conjuntos: Um contendo estudantes do curso de Python e um
# contando estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
# Alguns alunos que estudam Python tambem estudam Java

# Gerar conjunto com nome de todos estudantes, sem duplicidade.
# Forma 01 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
# Forma 02 - Utilizar o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 01 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)
# Forma 02 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que nao estao no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
# Alguns alunos que estudam Python tambem estudam Java

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
