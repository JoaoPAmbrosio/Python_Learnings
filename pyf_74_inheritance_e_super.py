"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender as classes.

OBS: Com a herança, a partir de uma classe existente, extende outra classe que passa a herdar atributos e metodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

cl1 = Cliente('Angelina', 'Jolie', '123.456.789-10', 5000)
fun1 = Funcionario('Felicity', 'Jones', '109,876,543-21', 1234)
print(cl1.nome_completo())
print(fun1.nome_completo())

# Utilizar formas genericas para reduzir codigo!
OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Qaudno uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    '''Cliente herda de Pessoa'''
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        # Forma comum de acessar super classe
        self.__renda = renda


class Funcionario(Pessoa):
    '''Funcionario herda de Pessoa'''
    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        # Forma incomum de acessar dados da super classe
        self.__matricula = matricula


cl1 = Cliente('Angelina', 'Jolie', '123.456.789-10', 5000)
fun1 = Funcionario('Felicity', 'Jones', '109,876,543-21', 1234)
print(cl1.nome_completo()) # R: Angelina Jolie
print(fun1.nome_completo()) # R: Felicity Jones

# Sobrescrita de método, ocorre quando é reescrito/reimplementado um método presente na super classe em classes filhas
"""
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    '''Cliente herda de Pessoa'''
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        # Forma comum de acessar super classe
        self.__renda = renda

class Funcionario(Pessoa):
    '''Funcionario herda de Pessoa'''
    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        # Forma incomum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        return f'Nome: {self._Pessoa__nome} Matricula: {self.__matricula}'


cl1 = Cliente('Angelina', 'Jolie', '123.456.789-10', 5000)
fun1 = Funcionario('Felicity', 'Jones', '109,876,543-21', 1234)
# Sobrescrita de método
print(cl1.nome_completo()) # R: Angelina Jolie
print(fun1.nome_completo()) # R: Nome: Felicity Matricula: 1234


"""
class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca

an1 = Gato('Joao', 'Felino', 'Ciames')
an1.faz_som('miuau') # R: O Joao fala miuau
"""
