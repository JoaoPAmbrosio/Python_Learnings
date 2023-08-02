"""
Built-In_Exceptions
https://docs.python.org/3/library/exceptions.html

Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução

Os erros mais comuns:

1- SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, voce escreveu algo que o Python não
reconhece como parte da linguagem.
Exemplo:

def funcao:
    print('Joao Ambrosio')

Usar palavras reservadas:
def = 1
return

2- NameError -> Ocorre quando uma variável ou funcao nao foi definida
# Exemplos NameError

print(x) - imprimir função que não existe
joao() - função que não existe


a = 5
if a < 4:
    msg = 'é maior que 10'
print(msg)
# Como a estrutura condicional não foi satisfeita, não entrou dentro dela e a variavel nao foi definido. Variavel local.
Para corrigir, defina ela antes!

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.
Exemplo TypeError
print(len(5))
print('Joao'+[])


4 - IndexError -> Ocorre quando tenta-se acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.
lista = ['Joao']
print(lista[2])
lista = ['Joao']
print(lista[0][10])

5 - ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto.
Exemplos ValueError
print(int('Joao'))

6 - KeyError -> Ocorre quadno tenta-se acessar um dicionário com uma chave que não existe.
Exemplos de KeyError
dict = {'joao': 'ambrosio'}
print(dict['python'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.
Exemplos AttributeError
tupla = [1, 2, 31, 4]
print(tupla.sort()) # Não existe este atributo em tuplas, mas somente em listas. AttributeError.

8 - IndentationError -> Ocorre quando não é respeitado a identação do Python de 04 espaços
Exemplos de IndentationError
def nova():
print('joao') # Errado
def nova():
    print('joao') # Correto

OBS: Exceptions e Erros são sinonimos na programação
importante ler e prestar atenção na saída de erro.
"""
for i in range(10):
print(i + 10)


