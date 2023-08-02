"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - Abre-se o arquivo
# 2 - Manipula o arquivo
# 3 - Fecha o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.


"""
# O bloco with - É a forma Pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readline())
    print(arquivo.closed) # R: False
print(arquivo.closed) # R: True



