"""
Trabalhando com deltas de data e hora
http://docs.python.org/3/library/datetime.html

    Trabalhado no arquivo: pyf_68_iterators_iterables_generators_yield.py
    import time
    gen_inicio = time.time()

data_inicial = dd/mm/yyyy 12:55:34.9939329
data_final = dd/mm/yyyy 13:34:23.0948484


import datetime
data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2024, 4, 14, 0)
tempo_para_evento = aniversario - data_hoje
print(type(tempo_para_evento)) # R:<class 'datetime.timedelta'>
print(repr(tempo_para_evento)) # R:datetime.timedelta(days=267, seconds=29646, microseconds=453753)
print(tempo_para_evento.days ) # R:267

# Boleto adicionando 3 dias
import datetime
data_da_compra = datetime.datetime.now()
print(data_da_compra) # R: 2023-07-21 15:47:42.211257
regra_boleto = datetime.timedelta(days= 3)
print(regra_boleto) # R:3 days, 0:00:00
vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto) # R: 2023-07-24 15:47:42.211257


# Com o now pode ser especificado um Timezone (fuso horario), com Today não é possível!
import datetime
agora = datetime.datetime.now()
print(agora) # R: 2023-07-21 15:52:04.456775
print(type(agora)) # R: <class 'datetime.datetime'>
print(repr(agora)) # R: datetime.datetime(2023, 7, 21, 15, 52, 4, 456775)

hoje = datetime.datetime.today()
print(hoje) # R: 2023-07-21 15:52:04.456775
print(type(hoje)) # R: <class 'datetime.datetime'>
print(repr(hoje)) # R: datetime.datetime(2023, 7, 21, 15, 52, 4, 456775)



# Organizar uma manutenção. Mudanças ocorrendo à meia-noite , combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao) # R: 2023-07-22 00:00:00
print(type(manutencao)) # R: <class 'datetime.datetime'>
print(repr(manutencao)) # R: datetime.datetime(2023, 7, 22, 0, 0)

# Encontrar o dia da semana. weekday()
# Os dias da semana do método weekday() começam em 0, sendo segunda-feira
# 0 - segunda-feira (Monday)
# 1 - terça-feira (tuesday)
# 2 - quarta-feira (wednesday)
# 3 - quinta-feira (thursday)
# 4 - sexta-feira (friday)
# 5 - sabado (saturday)
# 6 - domingo (sunday)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday()) # R:5

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
if aniversario.weekday() == 0:
    print('Voce nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Voce nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Voce nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Voce nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Voce nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Voce nasceu em uma sabado')
else:
    print('Voce nasceu em uma domingo')

20/01/1963 -> Voce nasceu em uma domingo

# Formatando datas/horas com strttime() (String Format Time)
# dd/mm/yyyy hora:minuto
hoje = datetime.datetime.now()
print(hoje)
hoje_formatado = hoje.strftime('%d/%B/%Y ')
# Y -> Ano completo (2023)
# y -> ano abreviado (23)
# m -> mes digito (07)
# b, nome mes abreviado->Jul
# B, nome mes completo->July
print(hoje_formatado)


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'
hoje = datetime.datetime.now()
print(hoje) # R: 2023-07-21 17:04:21.705536
print(formata_data(hoje)) # R: 21 de Julho de 2023

# Uso do TextBlob
http://textblob.readthedocs.io/en/dev
from textblob import TextBlob
def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(from_lang='en-us',to='pt-br')} de {data.year}"
hoje = datetime.datetime.now()
print(hoje) # R: 2023-07-21 17:17:40.535855
print(formata_data(hoje)) # R: 21 de Julho de 2023


nascimento = datetime.datetime.strptime('10/04/1998','%d/%m/%Y')
print(nascimento)
nascimento = input('Qual sua data de nascimento (dd/mm/yyyy): ')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)

# somente hora
almoco = datetime.time(12, 30, 0)
print(almoco)

import timeit
# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Loop for: {tempo}') # R: Loop for: 0.12022160005290061
# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(f'List Comprehension: {tempo}') # R: List Comprehension: 0.09327970002777874
# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(f'Map: {tempo}') # R: Map: 0.1074588000192307

"""
import functools
# Marcando tempo de execução de codigo com timeit

import timeit

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000)) # R: 6.584522299992386
# functools partial é para mostrar qual funcao que quer ser executada e parametro de entrada da funcao


