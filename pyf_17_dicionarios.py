"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}
print(type({}))
<class 'dict'>

OBS: Sobre Dicionários:
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podems misturar tipos de dados

# Criando dicionários
# Forma 01 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 02 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 01 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# OBS: Caso tente-se fazer acesso com uma chave inexistente, tem-se KeyError

# Forma 02 - Acessando via get (Recomendado)
x = input('Digite o codigo do pais:')
print(paises.get(f'br'))
print(paises.get(f'ru')) # None

x = input('pais? ')
# Exemplo 01
pais = paises.get(f'{x}')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')
# Caso o get não encotre o objeto com a chave informada será retornado o valor None e não
# será gerado KeyError

# Exemplo 02
# Pode ser definir um padrão caso nao encontre o objeto com a chave informada
pais = paises.get(f'{x}', 'Não encontrado')
print(f'País: {pais}')

# Pode ser verificado se determinada chabe se encontra em um dicionário
print('br'in paises) # True
print('ru'in paises) # False
print('Estados Unidos'in paises) # False, não é chave é valor (ele busca pela chave)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla dicionário,
# como chaves de dicionários.

# Tuplas são interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis.
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (35.7749, 122.4194): 'Escritório em São Paulo',
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

# Forma 01 - Mais comum
receita = {'jan': 100, 'fev': 120, 'mar':300}
# print(receita)
# print(type(receita))
z = 0
j = ''
while z == 0:
    x = input('digite o mes: ')
    x = x.lower()
    y = int(input('digite o valor: '))
    receita[f'{x}'] = y
    w = 0
    while w == 0:
        j = input('Voce quer adicionar um novo valor? Sim ou Nao: ')
        j = j.title()
        if j == 'Sim':
            w += 1
        elif j == 'Nao' or j == 'Não':
            z += 1
            break
        else:
            print('Voce digitou errado!')
print('Os valores em receita são:')
print(receita)

# Forma 02
receita = {'jan': 100, 'fev': 120, 'mar':300}
x = input('digite o mes: ')
x = x.lower()
y = int(input('digite o valor: '))
novo_dado = {f'{x}':y}
receita.update(novo_dado) # receita.update({'x2': y2})
print(receita)

receita = {'jan': 100, 'fev': 120, 'mar':300, 'abr':500}
# Atualizando dados em um dicionário
# Forma 01
print(receita)
receita['abr'] = 550
print(receita)

# Forma 02
receita.update({'abr': 100})
print(receita)

# Conclusão: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# Em dicionários, NÃO pode-se ter chaves repetidas

# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar':300, 'abr':500}
# Forma 01 - Mais comum
ret = receita.pop('mar')
print(receita)
print(ret)
# OBS 1: Aqui precisamos SEMPRE informar a chave,e caso não encontre o elemento, um KeyError é retornado
# OBS 2: Ao remover um objeto, o valor deste objeto é sempre retornado.

# Forma 02
del receita['fev']
print(receita)
# Neste caso o valor removido não é retornado
# Se a chave não existir, será gerado um KeyError

# Porque usar dicionário
# Exemplo 01: Imagine que tem um comércio eletrônico, onde tem um carrinho de compras na qual
# adicionamos produtos

Carrinho de compras:
    Produto 01:
        - Nome;
        - qualtidade;
        - preço;
    Produto 02:
        - nome;
        - quantidade;
        - preço;

# Utilizando em lista
# Tem que saber o índice de cada informação do produto.
carrinho = []
produto1 = ['playstation 4', 1, 2300.00]
produto2 = ['God of War', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Utilizando tupla
# Tem que saber o índice de cada informação do produto.
produto1 = ('playstation 4', 1, 2300.00)
produto2 = ('God of War', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)

# Utilizando dicionário
# Tem que saber o índice de cada informação do produto.
carrinho = []
produto1 = {'nome': 'playstation 4', 'quantidade': 1, 'valor': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'valor': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# print(produto1.get('valor'))
# print(carrinho[1])
# Como acessar infos de biblioteca dentro de lista?
# print(carrinho[1(produto1.get('valor'))]) # Codigo errado!

# Esta forma, evita vários problemas
# É facilmente adicionado ou removido produtos no carrinho e em cada produto
# se tem a certeza sobre cada informação

# Métodos de dicionários
D = dict(a=1, b=2, c=3)
print(D)
print(type(D))

# Limpar o dicionário (Zerar dados)
D = dict(a=1, b=2, c=3)
D.clear()
print(D)

# Copiando um dicionário para outro
# Forma 01 - Deep copy
D = dict(a=1, b=2, c=3)
novo = D.copy() 
print(novo)
novo['d']=4
print(D)
print(novo)

# Forma 02 - Shallow Copy
D = dict(a=1, b=2, c=3)
novo = D
print(novo)
novo['d']=4
print(D)
print(novo)


"""
# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
# O método fromkeys recebe dois parametros: um interável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
# {'t': 'valor', 'e': 'valor', 's': 'valor'}

veja = {}.fromkeys(range(1, 6), 'valor')
print(veja)
# {1: 'valor', 2: 'valor', 3: 'valor', 4: 'valor', 5: 'valor'}

