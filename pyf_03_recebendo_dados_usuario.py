"""
Recebendo dados do usuário
input() -> Todo dado recebido via imput é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas Simples triplas -> '''Angelina Jolie'''
"""
# - Aspas Duplas triplas -> ""Angelina Jolie"""


# Entrada de dados

# print("Qual seu nome?")
# nome = input()  #input -> entrada
nome = input('Qual seu nome? ')
nome = nome.title()

# Exemplo de print antigo
# print('Seja bem-vindo(a) %s'% nome)

# Exemplo de print moderno, a partir das versoes 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print mais atual 3.7
print(f"Seja bem-vindo {nome}.")

# print("Qual sua idade: ")
# idade = input()

idade = int(input("Qual sua idade? "))

# Processamento

# Saída de dados
# Exemplo de print antigo
# print("A %s tem %s anos" % (nome, idade))
# Exemplo de print moderno, a partir das versoes 3.x
# print("A {0} tem {1} anos".format(nome, idade))
print(f"A {nome} tem {idade} anos e nasceu em {2023 - idade}.")
"""
# int(idade) => cast

Cast é a conversão de um tipo de dado para outro.
"""
# print(f'A {nome} nasceu em {2023- int(idade)}.')
