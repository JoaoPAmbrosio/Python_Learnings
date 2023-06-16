"""
Funções co Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opicional;

# Exemplo de função onde a passagem de parâmetro seja opicional
print('Joao Ambrosio')
print()

Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado()) # TypeError



def exponecial(numero=4, potencia=2):
    return numero ** potencia


print(exponecial(2, 3)) # 2 * 2 * 2 = 8
print(exponecial(3, 2)) # 3 * 3 = 9
print(exponecial(3)) # Quando em uma função voce já coloca igualando a algum valor (como a potencia),
# adicionar outro se torna opicional. Se for informado, substituirá o valor pré determinado.
print(exponecial(3, 5))
# OBS: Se o usuario passar somente 01 argumento, este será atribuído ao parâmetro numero e será calculado
# o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parametro numero e o segundo ao parâmetro
# potencia. Entao será calculada esta funçao potência.
print(exponecial())

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.
def teste(potencia, num=2):
    return num ** potencia
print(teste(6))

# Outros exemplos
def soma(num1, num2):
    return num1 + num2
print(soma(4, 3)) # R: 7
print(soma(4)) # TypeError
print(soma()) # TypeError

# Exemplo mais complexto
def mostra_informacao(nome='Joao', instrutor=False):
    if nome == 'Joao' and instrutor:
        return 'Bem vindo instrutor Joao!'
    elif nome == 'Joao':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'
print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))

# Por quê utilizar parâmetros com valor default?
- Nos permite ser mais flexiveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc;

# Exemplos
def soma(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def mat(num1, num2, fun=soma):
    return fun(num1, num2)

print(mat(2, 3)) # R: 5
print(soma(2, 3)) # R: 5
print(mat(2, 2, subtracao)) # R: 0
print(subtracao(2, 2)) # R: 0

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Joao' # Variável Global, não faz parte de escopo de nenhuma variável

def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'
print(diz_oi())

# OBS: Se tivermos uma variável local com mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Joao' # Variável local
    return f'Olá {prof}'
print(diz_oi())
print(prof) # NameError -> Como é uma variável local, ela não é lida e tomado como inexistente.

total = 0
def incrementa():
    total = total +1 # UnboundLocalError -> A variável local está sendo utilizada para processamento sem ter sido inicializada.
    return total
print(incrementa())

# ATENÇÃO com variáveis globais (Se puder evitar, exite!)

total = 0
def incrementa():
    global total # Avisando que quer utilizar a variável global
    total = total +1
    return total
print(incrementa()) # R: 1
print(incrementa()) # R: 2
print(incrementa()) # R: 3


"""
# Pode se ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador # Utiliza a variavel contador, como nao global. nonlocal -> função anterior
        contador = contador +1
        return contador
    return dentro()

print(fora()) # R: 0
print(fora()) # R: 0
print(fora()) # R: 0

print(dentro()) # R: NameError fora do escopo
