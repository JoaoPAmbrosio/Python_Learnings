"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não se pode escrever. Apenas ler.
Da mesma forma, se abrir um arquivo para escrita, não é possivel ler, somente escrever.

# Ao abrir um arquivo para a escrita, o arquivo é criado no sistema operacional.

# Para escrever dados em um arquivo, após abrir o arquivo utiliza-se a função write().
Esta função recebe uma string como parâmetro, caso contrario tem-se um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso ele já exista, o anterior
será apagado e um novo será criado. Dessa forma, todo o conteúdo do arquivo anterior será perdido.

# Exemplo escrita - modo 'w' - write

# Forma tradicional de escrita em arquivo. Não Pythonica de se escrever!
arquivo = open('mais.txt', 'w')
arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais texto.\n')
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)

# Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    # arquivo.write('Escrever dados em arquivo é muito facil.\n')
    # arquivo.write('Pode-se colocar quantas linhas quiser.\n')
    # arquivo.write('Esta é a ultima linha.\n')
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros .\n')
    arquivo.write('Mas esta continua sendo a ultima linha.\n')


with open('novo.txt', 'w') as arquivo:
    arquivo.write('Joao' * 1000)
"""
with open('Frutas.txt', 'w') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ")
        fruta = fruta.title()
        if fruta != 'Sair':
            arquivo.write(fruta + '\n')
        else:
            break

