"""
Utilizando Lambdas  - integrated function

(Primeiro aprendizado em: "pyf_22_default_dict.py"

Conhecidas por Expressões Lambdas, ou simplesmente lambdas, são funções sem nome, ou seja,
funções anonimas.

# Função em Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' '+ sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE')) # R: Angelina Jolie
print(nome_completo('  FELICITY        ', 'jones')) # R:Felicity Jones

# Em funções Python pode-se ter nenhuma ou várias entradas. Em lambda também
amar = lambda: 'Como não amar Python? '
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1, x2, ......., xn: <expressão>
print(amar()) # R: Como não amar Python?
print(uma(6)) # R: 19
print(duas(5, 7)) # R: 5.916079783099616
print(tres(3, 6, 9)) # R: 4.909090909090908

# OBS: Se passar mais argumentos que parâmetros esperados tem-se TypeError

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    # Retorna a função f(x) = a * x ** 2 + b * x + c
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0)) # R: -5
print(teste(1)) # R: 0
print(teste(2)) # R: 9
print(geradora_funcao_quadratica(2, 3, -5)(2)) # R: 9



"""
# Exemplo PEGANDO SOBRENOME E COLOCANDO EM ORDEM ALFABÉTICA
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert He inlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(autores)
# print(autores.title()) # Nao funciona por ser `list` e nao `string`
autores = [i.title() for i in autores] # Utilizando List comprehension
print(autores)

# Utiliza o lambda na opcao do key, parametro de entrada
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) # Esse lower, teria funcao caso tivesse nomes em
# formatacao diferentes. Como todos ja passaram pelo title com list comprehension nao e necessario.
print(autores)

