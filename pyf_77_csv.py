"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Virgula

# Separador por vírgula
"joao", "ambrosio", "python", "ciencias", "dados"
1, 2, 3, 4, 5, 6

# Separador por ponto e virgula
"joao"; "ambrosio"; "python"; "ciencias"; "dados"
1; 2; 3; 4; 5; 6

# Separador por espaco
"joao" "ambrosio" "python" "ciencias" "dados"
1 2 3 4 5 6

http://dados.gov.br/dataset

# LENDO CSV

# Possivel de se trabalhar, mas não ideal
with open('lutadores.csv', encoding='utf-8') as file1:
    # encoding='utf-8' -> Como você está usando um sistema operacional de uso doméstico/comum, no caso o Windows, dentre
    # as centenas de problemas, falhas e limitações presentes neste sistema está o de codificação errada de caracteres.
    # Então temos que informar manualmente para que o arquivo seja aberto com a codificação correta.
    # Fazendo uso de sistemas operacionais de uso profissional na computação e programação como as distribuições Linux
    # ou o Mac OS não tem estes problemas.
    dados = file1.read()
    dados = dados.split(',')
    print(dados)


A Linguagem Python possui duas formas diferentes para ler dados em arquivo CSV:
    - reader -> Permite que itere sobre as linhas do arquivo CSV como listas;
from csv import reader
with open('lutadores.csv', encoding='utf-8') as file1:
    leitor_csv = reader(file1)
    next(leitor_csv)
    # print(list(leitor_csv)) # [['Nome', 'País', 'Altura (em cm)'], ['Ryu', 'Japão', '175'], ['Ken', 'EUA', '175'],....
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centrimetros')
    file1.seek(0)
    print(list(leitor_csv))

    - DictReader -> Permite que itere sobre as linhas do arquivo CSV como OrderedDicts;
from csv import DictReader
with open('lutadores.csv', encoding='utf-8') as file1:
    # CASO SEJA OUTRO SEPARADOR, IDENTIFICANDO QUAL
    leitor_csv = DictReader(file1, delimiter= ';')
    print(list(leitor_csv))
    file1.seek(0)
    next(leitor_csv)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']}")


# ESCREVENDO CSV

# writer() -> Gera um objeto para que possa ser escrito em um arquivo csv. Utiliza-se o método writerow() para escrever
# cada linha. Este método recebe uma lista.
from csv import writer
# Usando o newline='' com vazio para nao pular liha
with open('filmes.csv', 'w', newline='') as file1:
    escritor_csv = writer(file1)
    filme = None
    escritor_csv.writerow(['Títulos', 'Genero', 'Duração'])
    while filme != 'Sair':
        filme = input('Digite nome do filme: ')
        filme = filme.title()
        if filme != 'Sair':
            genero = input('Inforte o genero: ')
            duracao = input("informe a duração: ")
            escritor_csv.writerow([filme, genero.title(), duracao])

"""
# DictWriter

from csv import DictWriter
with open('filmes2.csv', 'w', newline='') as file1:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(file1, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'Sair':
        filme = input('Digite nome do filme: ')
        filme = filme.title()
        if filme != 'Sair':
            genero = input('Inforte o genero: ')
            duracao = input("informe a duração: ")
            escritor_csv.writerow({cabecalho[0]: filme, cabecalho[1]: genero.title(), cabecalho[2]: duracao})


# Aprendi a fazer, agora como imprimir o ordered dict?