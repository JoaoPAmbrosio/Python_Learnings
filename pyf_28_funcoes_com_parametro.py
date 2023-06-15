"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se pensar em um programa qualquer, geralmente tem-se:

entrada -> processamento -> saída

Se for pensado em uma função, já sabe-se que tem funlções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função


def quadrado(numero):
    # return numero * numero
    return numero **


print(quadrado(7))
print(quadrado(2))
# print(quadrado()) # TypeError -> Nao foi enviado o parametro


def cantar_parabens(aniversariante):
    print(f'Parabéns para você\nNesta data querida\nMuitas felicidades\nMuitos anos de vida\nViva o/a {aniversariante}!')


cantar_parabens('Patricia')

# Funções podem ter n parametros de entrada. Ou seja, podemos receber como entrada em uma função
# quantoas parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Joao '))
print(outra(5, 4, 'Ambrosio '))


# Se for informado um número errado de parâmetro ou argumentos, teremos um TypeError

# Nomeando parâmetros

def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'
print(nome_completo('Angelina', 'Jolie'))


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))
# Na execução nao muda em anda, mas na visualização tem muito ganho.

# A diferença entre Parâmetros e argumentos
# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!
nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso seja utilizado nomes dos parâmetros nos argumentos para informá-los, pode utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
"""
# Erro comum na utilização de return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
