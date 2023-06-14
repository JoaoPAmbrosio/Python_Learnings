"""
Definindo Funções

- Funções são pequenas pardes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar saídas de dados;
- Uteis para executar procedimentos simitares por repetidas vezes;

OBS: Se escrever uma função que realiza varias tarefas dentro dela;
É bom fazer uma verificação para que a função seja simplicada.

Se utiliza muitas funções:
- print()
- len()
- max()
- min()
- count()
- etc;

"""
# Exemplo de utilização de funções:
# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-In) do Python print():
# (é uma função que já vem na linguagem de programação)

# print(cores)
# print(help(print))

# DRY - Don't Repeat Yourself (princípio)

# Como definir funções

"""
Em Python, a forma geral de definir uma funçao é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou nao;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utiliza-se a palavra reservada 'def' informando ao Python que
esta sendo definido uma função. Também abre-se o bloco de código com o já conhecido dois pontos : que é
utilizado em Python para definir blocos.
"""
# Definindo a primeira função
# Exemplo 01


def diz_oi():
    print('oi!')


"""
OBS: 
1 - Veja que, dentro das funções pode-se utilizar outras funções;
2 - A função somente executa uma tarefa, ou seja, a unica coisa feita é dizer "oi!";
3 - A função não recebe nenhum parametro de entrada (nada dentro do parenteses) para ser executada;
4 - Essa função não retorna nda
"""
# Utilizando funções
diz_oi()
# Não pode ser esquecido o parênteses, logo em seguida da função. Ex: diz_oi ou diz_oi () -> Errado!

# Exemplo 02


def cantar_parabens():
    print('Parabéns para você\nNesta data querida\nMuitas felicidades\nMuitos anos de vida\nViva o aniversariante!')


# for n in range(5):
#     print(f'Esta é a vez numero {n+1} <><><>>')
#     cantar_parabens()

# Em Python, pode-se inclusive criar variáveis do tipo de uma função e executar esta função através da variável
canta = cantar_parabens
canta()
# É de certa forma, incomum. Em várias outras linguagens, não exite como em C e outras.
