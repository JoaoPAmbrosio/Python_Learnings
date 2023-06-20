"""
Entendendo o *args

- O *args é um parametro, como outro qualquer. Isso significa que voce poderá chmar de qualquer coisa, desde
que comece com asterisco.

Exemplo:
*xis

Mas por convenção, utiliza-se *args para defini-lo
O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Entao desde já lembre-se que tuplas são imutáveis

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6)) # R: TypeError
print(soma_todos_numeros(4, 6, 9, 5)) R: TypeError

# Entendendo o args
def soma_todos_numeros(nome, sobrenome, *args):
    return sum(args)

print(soma_todos_numeros('angelina', 'jolie'))
print(soma_todos_numeros('angelina', 'jolie', 1))
print(soma_todos_numeros('angelina', 'jolie', 1, 2))
print(soma_todos_numeros('angelina', 'jolie', 1, 2, 3))
print(soma_todos_numeros('angelina', 'jolie', 1, 2, 3, 4))

# Outro exemplo de utilização do *args
def verifica_info(*args):
    if 'Joao' in args and 'Ambrosio' in args:
        for nome in args:
            if nome == 'Joao':
                return f'Bem vindo {nome}'
    return 'Eu não tenho certeza quem voce é ...'
print(verifica_info())
print(verifica_info(1, True, 'Ambrosio', 'Joao'))
print(verifica_info(1, 'Ambrosio', 3.145))

"""
def soma_todos_numeros(*args):
    return sum(args)
print(soma_todos_numeros()) # R: 0
print(soma_todos_numeros(3, 4, 5, 6)) # R: 18
numeros = [4, 5, 6, 7] # Funciona com lista [], tupla (), sets {}. Somente dicionários que não {'x': 'y'}!
# print(soma_todos_numeros(numeros, 3, 4, 5)) # R: TypeError -> dados empacotados ([4, 5, 6, 7], 3, 4, 5)

# Desempacotador
print(soma_todos_numeros(*numeros)) # R: 22

# O asteriscos serve para que informemos ao Python que esta sendo passado uma coleção de dados.
# Desta formam ele sabeque é necessário desempacotar estes dados.




