"""
Listas (List)

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens, se voce criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tip de dado;

As listas em Python são representadas por colchetes: []

As listas são mutáveis: Ou seja, elas poodem mudar constantemente.

type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['J', 'o', 'a', 'o', ' ', 'A', 'm', 'b', 'r', 'o', 's', 'i', 'o']
lista3 = []
lista4 = list(range(11))
lista5 = list('Joao Ambrosio')


# Podemos facilmente checar se determinado valor esta contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('o'))

# Adicionar elementos em listas

Para adicionar elementos em lista, utilizamos a função append
OBS: Com append, nós só conseguimos adicionar 1 elemento por vez

print(lista1)
lista1.append(42)
lista1.append([8, 3, 1])
print(lista1)

if 8 in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Podemos inserir um novo elemento na lista informando a posiçao do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos juntar duas listas
lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)

# Podemos inverter uma lista, com reverse ou slice [::-1].
# Forma 01
lista1.reverse()
lista2.reverse()
# Forma 02
print(lista1[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

# Podemos remover o último elemento de uma lista
# OBS: O pop nao somente remove o ultimo elemento, como o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice serão deslocados para a esquerda
# Se não houver elemento no indice informado, será retornado erro IndexError
x = 2
lista5.pop(x)
print(lista5)

# Pode-se remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Pode-se repetir elementos de uma lista
nova = [1, 2, 3]
print(type(nova))
print(nova)
nova = nova * 3
print(nova)

 resposta:
<class 'list'>
[1, 2, 3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]

# Pode-se converter string para lista
# Exemplo 01
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)
#OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 02
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo esta sendo falado: Pega  lista6, coloca espaço entre cada element e transforma em uma string
curso = ' '.join(lista6)
print(curso)
curso = curso.split()
print(curso)

# Pode-se colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados.
lista6 = [1, 2.34, True, 'Joao', 'd', [1, 2, 3], 451616816]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 01 - Utilizando for
soma = ''
for elemento in lista2:
    print(elemento)
    soma += elemento
print(f'o valor da soma é {soma}')

# Exemplo 02 - Utilizando while
carrinho = []
produto = '' # tipo string

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair;")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

carrinho.sort() # MELHORAR A ORGANIZAÇÃO DOS DADOS
print(f'O(s) produto(s) selecionado(s): {carrinho}')

contagem = 0
for produto in carrinho:
    contagem +=1
    print(f'O protudo {contagem} é {produto}')

# Utlizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros =[num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
#           0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# É feito acesso aos elementos de forma indexada inversa
# Para entender melhor índice negativo, analogicamente, pense em um circulo.
print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
print(cores[-5]) # erro, pois nao existe

cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores1[indice])
    indice += 1

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

cores = list(enumerate(cores))
print(cores)
[(0, 'verde'), (1, 'amarelo'), (2, 'azul'), (3, 'branco')]

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)


# Outro métodos não tão importantes, mas também úteis
# Encontrar um índice de um elemento na lista
numeros = [5, 6, 7, 5, 8, 9, 10]
# Em qual índice da lista está o valor 6?
print(numeros.index(6))
# Em qual índice da lista está o valor 9?
print(numeros.index(9))
# OBS: Caso não tenha este elemento na lista, será apresentado erro
# print(numeros.index(19)) -> ValueError
# Em qual índice da lista está o valor 5?
print(numeros.index(5)) # São dois, então retorna o valor índice do primeiro
# Pode-se fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # Buscando a partir do indice 1
# Pode-se fazer uma busca dentro de um range, ou seja, qual indice comecar a busca
print(numeros.index(8, 3, 6))

# Revisar de slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]
# Trabalhando com slice de lista com o parâmetro 'inicio'
lista = [1, 2, 3, 4]
print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes
# Trabalhando com slice de lista com o parâmetro 'fim'
lista = [1, 2, 3, 4]
print(lista[1:4:2]) # Começa em 0 e vai até o indice 3-1, com passo de 2 em 2.

nomes = ['Joao', 'Ambrosio']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0] # Forma 01
print(nomes)
nomes = ['Joao', 'Ambrosio']
nomes.reverse() # Forma 02 - Pythonica
print(nomes)
nomes = ['Joao', 'Ambrosio']
print(nomes[::-1]) # Forma 03

# Como realizar soma, valor maximo, valor minimo e tamanho de uma lista.
# * Se os valores forem inteiros e reais
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) # Soma (apenas para valores inteiros e reais)
print(max(lista)) # Máximo (apenas para valores inteiros e reais)
print(min(lista)) # Menor valor (apenas para valores inteiros e reais)
print(len(lista)) # Tamanho (qualquer tipo de dado)

# Pode-se transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))
[1, 2, 3, 4, 5, 6]
<class 'list'>
tupla = tuple(lista)
print(tupla)
print(type(tupla))
(1, 2, 3, 4, 5, 6)
<class 'tuple'>

# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3, num4 = lista
print(num1)
print(num2)
print(num3)
# Se tiver um número diferente de elementos na lista ou variáveis para receber os dados, tem-se ValueError

# Copiando uma lista para outra ()Shallow Copy e Deep Copy)

# Forma 01 - Deep Copy
lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)
# Veja que ao utilizarmos lista.copy() copia-se os dados da lista para uma nova, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (Cópia profunda)


# Forma 02 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista # Cópia
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que foi utilizado a copia via atribuição e foi copiado os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificaçao se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy
"""
type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['J', 'o', 'a', 'o', ' ', 'A', 'm', 'b', 'r', 'o', 's', 'i', 'o']
lista3 = []
lista4 = list(range(11))
lista5 = list('Joao Ambrosio')

# Treino de programa próprio
while True:
    L = input('Em qual lista quer procurar? ')
    L = L.lower()
    if L == 'lista1':
        L = lista1
        break
    elif L == 'lista2':
        L = lista2
        break
    elif L == 'lista3':
        L = lista3
        break
    elif L == 'lista4':
        L = lista4
        break
    elif L == 'lista5':
        L = lista5
        break
    elif L == lista1 or L == lista2 or L == lista3 or L == lista4 or L == lista5:
        break
    else:
        print('Essa lista não existe, digite novamente')

print('Essa lista existe!')
while True:
    numero = int(input('Qual o número? '))
    # numero = numero.lower()
    if numero in L:
        print(f'Encontrei o numero {numero}')
        print(f'A posição de {numero} é {L.index(numero)}')
        print(L)
        break
    else:
        print(f'Não encontrei o numero {numero}')

# Código errado, tem que aprender a colocar lista em imput
# tem que aprender a remover o '' para colocar lista em maiusculo por exemplo
# nao sei como misturar lista int de string print(paises.get(f'{x}'))
