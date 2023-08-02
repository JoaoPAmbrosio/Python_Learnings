"""
O block try/except

Utiliza-se o bloco try/except parar tratar erros que podem ocorrer no codigo. revinindo assim que o programa pare de
funcionar e o usuário receba mensagens inesperadas.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico
try:
    joao()
    # NameError!!
except:
    print('Deu algum problema')
# Tente executar a funçao joao(), caso encontre erros, execute except e imprima a mensagem de erro.

# Exemplo 2 - Tratando um erro genérico
try:
    len(5)
except:
    print('Deu algum problema')
# Tente executar a funçao len(), caso encontre erros, execute except e imprima a mensagem de erro.
OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma
específica.

# Exemplo 3 - Tratando um erro específico
# Erro:
try:
    len(5) # TypeError
except NameError:
    print('Voce está utilizando uma função inexistente')
# R: TypeError: object of type 'int' has no len()
# Tratando erro:
try:
    geek() # Name error
except NameError:
    print('Voce está utilizando uma função inexistente')
# R: Voce está utilizando uma função inexistente

# Exemplo 4 - Tratando um erro específico com detalhe do erro
try:
    len(5) # TypeError
except TypeError as err:
    print(f'A aplicação gerou seguinte erro: {err}')
# R: A aplicação gerou seguinte erro: object of type 'int' has no len()

# Exemplo 5 - Pode ser feito diversos tratamentos de erros de uma vez.
try:
    # len(5) # R: Deu TypeError: object of type 'int' has no len()
    # geek() # R: Deu NameError: name 'geek' is not defined
    print('Joao'[8]) # R: Deu um erro diferente (IndexError)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')


"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
# return None é vazio, retorna nada


dic = {"carro": "Porche", "nome": "Joao"}

print(pega_valor(dic, 'leao'))

