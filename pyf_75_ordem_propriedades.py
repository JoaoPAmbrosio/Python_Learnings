"""
POO - Propriedades - Properties

Contrução (ordem): Declarar classe, atributos de classe, contrutor, atributos de instancia, propertys, métodos de
instancia

Em linguagens de programação como o Java, ao declarar atributos privados nas clases, contuma-se a criar métodos públicos
para manipulação desses atributos. Esses métodos são conhecidos por getters e setters, onde os getters retornam o valor
do atributo e os setters alteram o valor do mesmo.

class Conta:

    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de R$ {float(self.__saldo)} do Cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    def get_numero(self):
        return self.__numero
    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    def set_limite(self, novo_limite):
        self.__limite = novo_limite

cc1 = Conta('Felicity', 3000, 5000)
cc2 = Conta('Angelina', 2000, 4000)

# Como somar os saldos das suas contas?
# Forma errada:
print(cc1._Conta__saldo + cc2._Conta__saldo)
# Forma correta:
print(cc1.get_saldo()+cc2.get_saldo())

Foi feito bem no estilo Java, agora será refatorado usando no estilo python


"""
class Conta:

    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
    # Properties do tipo setters, para alterar os valores

    def extrato(self):
        return f'Saldo de R$ {float(self.__saldo)} do Cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor


cc1 = Conta('Felicity', 3000, 5000)
cc2 = Conta('Angelina', 2000, 4000)


print(cc1.saldo+cc2.saldo)
print(cc1.__dict__)
# R:{'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 5000}
cc1.limite = 4321
print(cc1.__dict__)
# R:{'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 4321}
print(cc1.limite) # R:4321


