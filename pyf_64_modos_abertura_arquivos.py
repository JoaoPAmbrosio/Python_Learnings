"""
Modos de abertura de Arquivo

r (read)-> Abre para leitura - padrão
w (write)-> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir.
    Caso o arquivo exista, gera FileExistError
a (append) -> Abre para escrita, adicionando o conteúdo SEMPRE ao final do arquivo.
    Com módulo 'a' não se controla o cursor
+ -> Abre para modo de atualização leitura ou escrita
r+ -> Sobrescreve o que ta sendo escrito no topo. Caso o sobrescrito seja menor, parcela do anterior mantem
w+ -> Deleta o antigo arquivo e escreve o que esta sendo proposto.

http://docs.python.org/3/library/funcion.html#open

# Exemplo x

filename = 'Ambrosio'
try:
    with open(f'{filename}.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 3.\n')
except FileExistsError:
    print('Arquivo já existe!')


# Exemplo a - Adiciona SEMPRE no final
with open('Frutas.txt', 'a') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ")
        fruta = fruta.title()
        if fruta != 'Sair':
            arquivo.seek(0)
            arquivo.write(fruta + '\n')
        else:
            break

"""

print(open('Frutas.txt', 'r'))

with open('Frutas.txt', 'a') as arquivo:
    arquivo.write('No topo!\nNova linha.\nMais uma linha.\n')
'''
x= input("Digite 'novo' para novo arquivo ou 'adicionar' para adicionar conteudo? ")
cod = ''
x= x.lower()
if x == 'novo' or x == 'adicionar':
    if x == 'novo':
        cod = 'w'
    elif x == 'adicionar':
        cod = 'a'
    with open('Frutas.txt', cod) as arquivo:
        while True:
            fruta = input("Informe uma fruta ou digite 'sair': ")
            fruta = fruta.title()
            if fruta != 'Sair':
                arquivo.write(fruta + '\n')
            else:
                break
else:
    print('Não entendi o que quer fazer com o programa. Repita!')
'''