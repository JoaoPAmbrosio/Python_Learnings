"""
**kwargs

Poderia chamar esse parâmetro de **xis, mas por convenção este parâmetro é chamado de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs
exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário

# Exemplo 01


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
# Nem os parâmetros *args e **kwargs não são obrigatórios.
cores_favoritas()
cores_favoritas(joao='navy')

# Exemplo 02 - mais complexo


def cumprimento_especial(**kwargs):
    if 'Joao' in kwargs and kwargs['Joao'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Joao!'
    elif 'Joao' in kwargs:
        return f"{kwargs['Joao']} Joao!"
    return 'Não tenho certeza quem voce é'


print(cumprimento_especial()) # R: Não tenho certeza quem voce é
print(cumprimento_especial(Joao='Python')) # R: Você recebeu um cumprimento Pythônico Joao!
print(cumprimento_especial(Joao='Oi')) # R: Oi Joao!
print(cumprimento_especial(Joao='Especial')) # R: Especial Joao!

# Nas funções pode se ter (NESTA ORDEM):
- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

# Exemplo
#           param obrigatorios/*args/não obrigatorios/**kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print(f'O(a) {nome} é solteiro(a)')
    else:
        print(f'O(a) {nome} é casado(a)')
    print(kwargs)


minha_funcao(8, 'Julia') # R: Julia tem 8 anos, O(a) Julia é casado(a)
minha_funcao(18, 'Felicity', 4, 5, 6, solteiro=True) # R: Felicity tem 18 anos, (4, 5, 6), O(a) Felicity é solteiro(a)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai') # R:Felipe tem 34 anos, O(a) Felipe é casado(a), {'eu': 'Não', 'voce': 'Vai'}
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True) # R:Carla tem 19 anos, (9, 4, 3), O(a) Carla é casado(a), {'java': False, 'python': True}

# Entendendo o por quê é importante manter a ordem dos parâmetros na declaração
# Função com a ordem correta de parâmetros:


def mostra_info(a, b, *args, instrutor='Joao', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='Ambrosio', cargo='Instrutor')) # R: [1, 2, (3,), 'Joao', {'sobrenome': 'Ambrosio', 'cargo': 'Instrutor'}]

# Função com a ordem incorreta de parâmetros, que normalmente é mais utilizado pelas pessoas:


def mostra_info(a, b, instrutor='Joao', *args, **kwargs):
    return [a, b,args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='Ambrosio', cargo='Instrutor')) # R:[1, 2, (), 3, {'sobrenome': 'Ambrosio', 'cargo': 'Instrutor'}]
"""

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(nomes) # R:{'nome': 'Felicity', 'sobrenome': 'Jones'}
# print(mostra_nomes(nomes)) # R: TypeError, nomes empacotado
print(mostra_nomes(**nomes)) # R: Felicity Jones
# A partir do duplo asteriscos (**), desempacota um dicionário


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


# Um asterisco (*) desempacota lista/tupla/set.
lista = [1, 2, 3]
tupla = (1, 2, 3)
set_conjuntos = {1, 2, 3}
# Um asterisco (*) desempacota lista/tupla/set.
soma_multiplos_numeros(*lista) # R:6
soma_multiplos_numeros(*tupla) # R:6
soma_multiplos_numeros(*set_conjuntos) # R:6
# Dois asteriscos (**) desempacotm dicionarios.
dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario) # R:6

# OBS! Os nomes da chave em um dicionario devem ser os mesmos dos parametros da função
dicionario = dict(d=1, e=2, f=3)
# soma_multiplos_numeros(**dicionario) # R:TypeError
