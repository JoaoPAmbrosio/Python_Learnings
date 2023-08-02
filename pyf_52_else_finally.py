"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!
Você é responsável pelas entradas das suas funções.
OBS: A função do usuário é DESTRUIR seu sistema.

# Else -> É executado somente se não ocorrer o erro
try:
    num = int(input('Informe um número: '))
    print(f'Voce digitou {num}')
except ValueError:
    print('Valor incorreto!')
else:
    print('Entrando no Else')

# Finally
# OBS: O bloco finally é sempre executado. Independente se houve exceção ou não.
# Finally geralmente é utilizado para fechar ou deslocar recursos.
try:
    num = int(input('Informe o número: '))
except ValueError:
    print('Voce digitou um valor inválido')
else:
    print(f'Voce digitou {num}')
finally:
    print('Executando o finally')

# Exemplo mais complexo - Forma Genérica
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Voce digitou valor errado!'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

# Mais simples, mas não tem o tratamento exclusivo para os erros que existem

# Exemplo mais complexo - Forma Semi-Genérico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Voce digitou valor errado! {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))


"""
# Exemplo mais complexo - Forma Pythonica
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return 'Não é possível realizar divisão por zero. \nDigite outro número!'
    except ValueError:
        return 'Voce digitou valor errado!\n O valor precisa ser numérico.'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))







