"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java
For(int i = 0; i< limitador; i++){
    //execução do loop
}

Python
for item in interável;
    ///execução do loop

Utilizamos loops para iterar sequências ou sobre valores iteráveis
Exemplo de iteráveis:
- String
    nome = 'Joao Ambrosio'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
    # Exemplo de for 01 (Iterando sob uma string)

for letter in nome:
    print(letter)

# Exemplo de for 02 (Iterando sobre uma lsita)
for numero in lista:
    print(numero)

range(valor_inicial, valor_final)
OBS: O valor final não é inclusive

# Exemplo de for 03 (Iterando sobre um range)
for numero in range(1, 11):
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])

for i, _ in enumerate(nome):  # Quando o indice ou letra nao sao importantes pode usar o "_".
    print(i)
for i in enumerate(nome):    # Mesma coisa
    print(i[0])

nome = 'Joao Ambrosio'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for i in enumerate(nome):
    print(i)

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Joao Ambrosio'
for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
Tabela de Icons: https://lordicon.com/icons
"""

# Original: U+1F60D
# Modificado: U0001F60D

nome = '\U0001F60D'

for x in range(3):
    for num in range(1, 11):
        print(f'{nome * num}')

