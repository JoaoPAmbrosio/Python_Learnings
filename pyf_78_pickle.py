"""
Conhecendo Pickle

A funcao do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar com arquivos pickle
vindos de outras pessoas que voce não conheça ou de fontes desconhecidas.


# Fazendo escrita em arquivo Pickle
garfield = Gato('Garfield')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as file1:
    # 'wb' o 'b' foia dicionado porque o objetivo é ser em binario
    # Dump recebe dois parametros: Objeto python (no nosso caso uma tupla com os dados) e o arquivo o qual quer escrever
    pickle.dump((garfield, pluto), file1)


"""
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} esta comendo...')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} esta miando...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo...')

# Fazendo leitura de dados em arquivo Pickle

with open('animais.pickle', 'rb') as file1:
    # Como é arquivo binario é necessario o 'b' no modo, ficando 'rb'
    # print(file1.read())
    # Se somente for lido, o arquivo apresenta em binario e é codigicado.
    # print(pickle.load(file1))
    # (<__main__.Gato object at 0x0000027C878E5150>, <__main__.Cachorro object at 0x0000027C878E64D0>)
    # load que descompacta o arquivos
    gato, cachorro = pickle.load(file1)
    print(gato.nome) # Garfield
    gato.comer() # Garfield esta comendo...
    gato.mia() # Garfield esta miando...

