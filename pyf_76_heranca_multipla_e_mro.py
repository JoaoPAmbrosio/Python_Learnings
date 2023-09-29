"""
POO - Heranca Multipla

Herança Multipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes, fazendo com que a classe
filha herde todos os atributos e métodos de todas as classes herdadas.
OBS: A heranca multipla pode ser feita de duas maneiras.
    - Por Multiderivação Direta;
    - Pr Muktuderivação Indireta;

# Exemplo 1 - Multiderivação Direta
class Base1:
    pass
class Base2:
    pass
class Base3:
    pass
class MultiDerivada(Base1, Base2, Base3):
    pass

# Exemplo 2
class Base1:
    pass
class Base2(Base1):
    pass
class Base3(Base2):
    pass
class MultiDerivada(Base3):
    pass
# Recebe diretamente Base3, mas indiretamente as outras Bases

OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos e
métodos das super classes.

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimento(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguin(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)

# Testando
baleia = Aquatico('Wally')
print(baleia.cumprimento())

tatu = Terrestre('Sandwish')
print(tatu.cumprimento())

p1 = Pinguin('Happy feet')
print(p1.andar())
print(p1.nadar())

print(p1.cumprimento())

----------------------------------------------------------
POO - MRO - Method Resolution Order

Method Resolution Order(Resolução de Ordem de Métodos) é a ordem de execução dos métodos(Quem será executado primeiro).

Em Python, pode ser conferido a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedades de classe __mro__
    - Via método mro()
    _ Via help

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimento(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

# Testando
p1 = Pinguim('Happy feet')
print(p1.cumprimento())

'''
- class Pinguim(Aquatico, Terrestre):
R: Eu sou Happy feet do mar!

class Pinguim(Terrestre, Aquatico):
R: Eu sou Happy feet da terra!
'''

Pinguim.mro() # R: (Apenas no console Python)
# R: [<class 'pyf_76_heranca_multipla_e_mro.Pinguim'>, <class 'pyf_76_heranca_multipla_e_mro.Terrestre'>, <class 'pyf_
# 76_heranca_multipla_e_mro.Aquatico'>, <class 'pyf_76_heranca_multipla_e_mro.Animal'>, <class 'object'>]

-------------------------------------------------------------------------
POO - Polimorfismo

Poli -> Multiplas
Morfis -> Formas

class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} late')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} mia')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
#    def falar(self):
#        print(f'{self._Animal__nome} faz barulho de roedor')

# Testando

sony = Cachorro('Sony')
sony.comer()
sony.falar()

charlin = Gato('Charlin')
charlin.comer()
charlin.falar()

stuart = Rato('Stuart')
stuart.comer()
# stuart.falar() aqui da problema

---------------------------------------------------------------------------
POO - Métodos Mágicos

Métodos Mágicos, são toos métodos que utilizam dunder.

dunder init -> __init__()

Dunder -> Doeble Underscore

dunder repr -> Representação do objeto
    def __repr__(self):
        return self.titulo

# Sem dunder repr
# print(lvro1) # R: <__main__.Livro object at 0x000001B0A7CF4A90>
# print(lvro2) # R: <__main__.Livro object at 0x000001B0A7CF4AD0>

# Adicionando o def __repr__(self):
print(lvro1) # R: Python Rocks!
print(lvro2) # R: Inteligencia Artificial com Python

dunder str - > Representa o objeto e tem prioridade sob o dunder repr
    def __str__(self):
        return self.titulo
print(lvro1) # R: Python Rocks!
print(lvro2) # R: Inteligencia Artificial com Python

"""
class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            return f'{self.paginas * other}'
        if isinstance(other, Livro):
            return f'{self.paginas * other.paginas}'
        return 'Não é possivel multiplicar'

lvro1 = Livro('Python Rocks!', 'Univesidade dados', 400)
lvro2 = Livro('Inteligencia Artificial com Python', 'Universidade dos dados', 350)

# print(len(lvro1)) # R: 400
# print(len(lvro2)) # R:350

print(str(lvro1.titulo) +' - '+  str(lvro2.titulo))
print(lvro1+lvro2)
print(lvro1*lvro2)
