"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python. utilizamos a função integrada open(), que significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parametro de entrada, que neste caso é o nome de
arquivo a ser lido. Essa função retorna um _io.TextIWrapper e é com ele que se trabalha.

https://docs.python.org/3/library/functions.html#open

#OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou se tem FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
_io.TextIOWrapper -> Tipo do arquivo
mode='r'-> Modo de Leitura. r -> read() -> ler
encoding='cp1252' -> Codificação que o arquivo esta escrito (caracteres, caracteres especiais, lingua, etc)
"""
arquivo = open('texto.txt')

# print(arquivo) # R:<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
# print(type(arquivo)) # R: <class '_io.TextIOWrapper'>

# Para ler o conteúdo de um arquivo, após sua abertura, deve-ser utilizar a função read()
# A função read() lê todo o conteúdo do arquivo.

ret = arquivo.read()

print(type(ret)) # R: <class 'str'>
print(ret)

# OBS: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor, funciona como o cursor
# quando se esta sendo escrito.
