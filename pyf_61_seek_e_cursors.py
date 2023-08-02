"""
Seek and Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo

# Movimentando o cursor pelo arquivo com a função seek()
# seek() -> Recebe um parâmetro que indica onde se quer colocar o cursor.

arquivo = open('texto.txt')
print(arquivo.read())
arquivo.seek(0)
print(arquivo.read())
arquivo.seek(20)
print(arquivo.read())

arquivo = open('texto.txt')

# readline() -> Função que le arquivo linha a linha
ret = arquivo.readline()
print(type(ret)) # R: <class 'str'>
print(ret.split(' '))

# readlines() -> Função que transforma o texto em uma lista, sendo que cada linha é dividida como um elemento da lista.

linhas = arquivo.readlines()
print(type(linhas)) # R: <class 'list'>
print(len(linhas))

# OBS: Quando se abre um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o
programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo deve-se fechar esta conexão.
Para isso utilizamos a funçao close()

Passos para se trabalhar com um arquivo.
1- Abrir o arquivo;
2- Trabalhar com o arquivo;
3- Fechar o arquivo;



"""
# 1- Abrir o arquivo;
arquivo = open('texto.txt')

# 2- Trabalhar com o arquivo;
print(arquivo.read())

# Verifica se o arquivo está aberto ou fechado (True or False)
print(arquivo.closed) # False

# 3- Fechar o arquivo;
arquivo.close()

print(arquivo.closed) # True

# print(arquivo.read())
# OBS: Se for tentado manipular o arquivo após seu fechamento, tem-se um ValueError




