""""
Funções de maior grandeza - Higher Order Functions - HOF

- Quando há uma linguagem de programação suporte HOF, indica que pode-se ter funções que retornam outras funções como
resultados ou mesmo que pode-se passar funções como argumentos para outras funções, e até mesmo criar variáveis do
tipo de funções nos programas.

Utilizado na seção de funções
Em Python, as funções são Cidadãos de Primeira Classe, First Class Citizens

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando funções
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas
Em Python também é possivel ter funções dentro de funções, conhecidas por Nested Functions ou Inner functions

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce '))
    return humor() + pessoa

print(cumprimento('Angelina'))
print(cumprimento('Felicity'))

Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahah', 'kkkkkkkk', 'kakakakakak'))
    return rir()
# Teste
rindo = faz_me_rir()
print(rindo)

Inner functions (Funções internas / Nested functions) podem acessar o escopo de funções mais externas.
from random import choice
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahah', 'kkkkkkkk', 'kakakakakak'))
        return f'{risada} {pessoa}'
    return dando_risada()
print(faz_me_rir_novamente('Angelina'))


Decoradores - (Decorators)

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
                               |-------------------------|
|-------------------------|    |   |------------------|  |
|    Function Decorator   | -> |   | Função decorada  |  |
|-------------------------|    |   |------------------|  |
                               |-------------------------|
Decorator como funções (Sintaxe não recomendada / Sem açucar sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce! ')
        funcao()
        print('Tenha um otimo dia! ')
    return sendo
def saudacao():
    print('Seja bem vindo ao curso')
# Teste
teste = seja_educado(saudacao)
teste()

# Testando 2
def raiva():
    print('EU TE ODEIO! ')
raiva_educada = seja_educado(raiva)
raiva_educada()

# Decorators com Syntax Sugar (Açucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce! ')
        funcao()
        print('Tenha um excelente dia! ')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Joao')

# Testando o decorator
apresentando()
@seja_educado_mesmo
def dormir():
    print('Quero dormir.. ')
dormir()

|---------------------------------------------------------------|
|   Home    |   Serviços    |   Produtos    |   Administrativo  |
|---------------------------------------------------------------|

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/serviços
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin
# OBS: Não é código funcional (Que funcione) é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')
def home(request):
    return 'Pode acessar home'
def serviços(request):
    return 'Pode acessar serviços'
def produtos(request):
    return 'Pode acessar produtos'

!!!Decorator!!!
@checa_login
def admin(request):
    return 'Pode acessar admin'
# OBS: Não confunda Decorator com Decorator Function

Decorator com diferentes assinaturas
# Para resolver, utiliza-se um padrão de projetos chamado Decorator Pattern
A assinatura de uma funçlão é representada pelo seu retorno, nome e parâmetros de entrada

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar
@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

print(ordenar('Picanha', 'Batata Frita'))
# R: TypeError: gritar.<locals>.aumentar() takes 1 positional argument but 2 were given

# SOLUCIONANDO
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar
@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'
print(ordenar('Picanha', 'Batata Frita'))
print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento preisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento preisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna
@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)
# o que esta sendo feito é: Pode informar quantos pratos quiser, pelo args, mas o primeiro deve ser 'pizza'.

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando
print(soma_dez(10, 12)) # 22
print(soma_dez(1, 21)) # Valor incorreto! Primeiro argumento preisa ser 10

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('hamburger', 'pizza'))

Forçando tipos de dados com decorators

zip -> a = (1, 3, 5) | b = (2, 4, 6)
c = zip(a, b) = (1, 2), (3, 4), (5, 6)
"""

def forca_tipo(*tipos):
    def decorator(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorator
@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(int(vezes)):
        print(msg)
repete_msg('Joao', '3')
@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)
dividir('1', 5)
