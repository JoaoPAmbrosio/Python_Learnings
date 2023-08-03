"""
POO - Abstracao e Encapstulamento

O grande objetivo da POO (programacao orientada ao objeto) é encapsular os códigos dentro de um grupo lógico e
hierárquico utilizando classes.


"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de R$ {float(self.__saldo)} do titular {self.__titular} com limite de R$ {float(self.__limite)}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor precisa ser positivo')

    def sacar(self, valor):
        if self.__saldo >= valor:
            if valor > 0:
                self.__saldo -= valor
            else:
                print('Valor precisa ser positivo')
        else:
            print(f'Valor não possue {(float(valor))} reais em conta!')

    def transferir(self, valor, conta_destino):
        # 1- Removendo valor da conta origem
        self.__saldo -= valor
        # 2 - Adicionando valor na conta destino
        conta_destino.__saldo += valor
        print(f'Saldo atual:\nValor transferido: R$ {float(valor)}\nConta {self.__titular}: {self.__saldo}. Conta {conta_destino.__titular}: {conta_destino.__saldo}')

cc1 = Conta('Joao', 150, 1500)
cc2 = Conta('Felicity', 300, 2000)
Conta.extrato(cc1)
Conta.extrato(cc2)

Conta.transferir(cc2, 250, cc1)
