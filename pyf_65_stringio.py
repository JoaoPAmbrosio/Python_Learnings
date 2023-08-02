"""
StringIO

ATENÇÂO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.

"""
# Primeiro fazemos o import
from io import StringIO

mensagem = 'Este é apenas uma string normal'

# Pode-se criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserir texto depois
arquivo = StringIO(mensagem)
# arquivo = open('Arquivo.txt', 'w') -> Equivalentes

# Agora tendo o arquivo
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Movimentar o cursor e fazer nova leitura
arquivo.seek(0)
print(arquivo.read())
