"""
JSON e Pickle

JSON -> JavaScript Object Notation

arquivos json são como dicionarios com chaves e valores

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (desenvolvedores).

import json
ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])
print(type(ret)) # <class 'str'>
print(ret) # ["produto", {"Playstation 4": ["2TB", "Novo", "220V", 2340]}]
# Foi colocando no input aspas simples e o resultado veio com as aspas duplas. O json formatou tudo em formato json

import json
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

garfield = Gato('Garfield', 'viralata')
print(garfield.__dict__) # {'_Gato__nome': 'Garfield', '_Gato__raca': 'viralata'}
print(json.dumps(garfield.__dict__)) # {"_Gato__nome": "Garfield", "_Gato__raca": "viralata"}

pip install jsonpickle

garfield = Gato('Garfield', 'viralata')
ret = jsonpickle.encode(garfield)
print(ret)

import jsonpickle
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

garfield = Gato('Garfield', 'viralata')
# Escrevendo de um objeto Python -> JSON
with open('ao_feliz.json', 'w') as file1:
    ret = jsonpickle.encode(garfield)
    file1.write(ret)

"""
import jsonpickle
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

garfield = Gato('Garfield', 'viralata')
# Escrevendo de um objeto Python -> JSON
with open('ao_feliz.json', 'r') as file1:
    conteudo = file1.read()
    ret = jsonpickle.decode(conteudo)
    print(type(ret)) # <class '__main__.Gato'>
    print(ret.nome) # Garfield
    print(ret.raca) # viralata

# Escrevendo de um objeto JSON -> Python

