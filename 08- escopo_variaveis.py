"""
Escopo de variáveis

Dois casos e escopo:

1 - Variávies globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreeende,todo o o programa.

2 - Variáveis Locais;
    - Variáveis locais são reconhjecidas apenas no bloco onde foram declaradas,
    ou seja, seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

A reatribuição não é permitido ao dado em C e em Java, diferente do Python

"""

numero = 42
print(numero)
print(type(numero))

numero = 'Joao'
print(numero)
print(type(numero))

numero = 42   # Exemplo de variável global
novo = 0     # Exemplo de variável global

if numero > 10:
    novo = numero + 10        # Exemplo de variável Local
    print('novo = %g'%(novo))

print(novo)

