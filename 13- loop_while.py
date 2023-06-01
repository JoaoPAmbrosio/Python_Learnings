"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

    O bloco do while será repedito enquanto a expressão booleana for verdadeira.

Expressao Booleana é toda expressão onde o resultado é verdadeiro ou falso

# Exemplo 01
numero = 1
while numero < 10:
    print(numero)
    numero += 1

# Em um loop while é importante que cuidemos de um critério de parada para não causar um loop infinito

# C ou Java

while(expressão){
    //execução
}

"""
#Exemplo 02

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou jessica? ')
