"""
Programação Orientada ao Objeto - POO

- POO é um paradigma de programação que utiliza que mapeamento de objetos do mundo real para modelos computacionais.
- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da Orientação ao Objetos
- Classes -> Modelo do objeto do mundo real sendo representado computacionalmente;
- Atributo -> Características do objeto.
- Método -> Comportamento do objeto (funções).
- Construtor -> Método especial utilizado para criar os objetos;
- Objeto -> Instância da classe.

numero = 10
print(numero) # R: 10
print(type(numero)) # R: <class 'int'>

class Produto:
    pass
ps4 = Produto()
print(ps4) # R: <__main__.Produto object at 0x00000196826544D0>
print(type(ps4)) # R: <class '__main__.Produto'>

POO - Classes

Em POO, classes nada mais são que modelos dos oibjetos do mundo real sendo representados computacionalmente.

Fazendo um sistema para automatizar o controle das lâmpadas da sua casa.

idade = 32
preco = 2340.45
nome = 'Felicity Jones'
print(type(idade)) # R: <class 'int'>
print(type(preco)) # R: <class 'float'>
print(type(nome)) # R:<class 'str'>

class Lampada:
    pass
lamp = Lampada()
print(type(lamp)) # R:<class '__main__.Lampada'>

Classes podem conter;
    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos consegue-se representar computa-
    cionalmente os estados de um objeto. No caso da lâmpada, possívelmente desejaria entender as caracteristicas da lâm-
    pada, como voltagem, calorimetria, cor, etc.
    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no
    sistema. no caso da lâmpada, por exemplo, um comportamento comum seria o ligar e desligar a mesma.

Em Python para definir uma classe, utiliza a palavra reservada class.

OBS: Utiliza-se a palabra 'pass' em Python quando tem-se um bloco de código que ainda não está implementado.
OBS: Quando nomea-se clsses próprias* em Python utiliza-se por convenção o nome com a inicial em maiúsculo. Se for nome
composto, utiliza-se iniciais de ambas as palavras em maiúsculo, todas juntas.
* as classes internas do Python (int, float, etc) são feitas em minúsculo, sendo facil entender as classes criadas, das
integradas. Objetivo é a facil diferenciação.

Dica: Em computação não se usa: Acentuação, caracteres especiais, espaços ou similares para nomes de classes atributos,
métodos, arquivos, diretorio e etc.

Quando esta sendo planejado um software e define-se quais classes terá no sistema, chama-se estes objetos que serão
mapeados para classes, de entidades.

POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos, consegue-se representar
computacionamente os estados de um objeto.

Em Python, se divide os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do método  construtor.
OBS: Método contrutor: É um método especial utilizado para a construção do objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria aproximadaments:

public class Lampada(){
    private int voltagem;
    private String cor;
    private String calorimetria
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor, String calorimetria){
        this.voltagem = voltagem;
        this.cor = cor;
        this.calorimentria = calorimetria;
    }

    public int getVoltagem(){
        return this.voltagem;
    ...
    ...
    ...
}

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é publico. Ou seja, pode ser acessado em
todo o projeto. Caso queira demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser
acessado/utilizado somente dentro da propria classe onde está declarado, utiliza-se __duplo underscore no inicio do nome
Isso é conhecido como Name Mangling.

class Lampada:

    def __init__(self, voltagem, cor, calorimetria):
        self.voltagem = voltagem
        self.cor = cor
        self.calorimetria = calorimetria
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que seja feito acesso aos
# atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')
print(user.email) # R: user@gmail.com
# print(user.__senha) # R: AttributeError: 'Acesso' object has no attribute '__senha'

print(user._Acesso__senha) # R: 123456
# Tem o acesso, mas não deveria fazê-lo. (Name Mangling)


user.mostra_email()
user.mostra_senha()

# O que significa atributos de instancia?
# Significa, que ao criarmos instancias/objetos de uma classe, todas as instâncias terão estes atributos

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '7891011')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

class Produto:

    # Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        # Atributos de instancia
        self.id = Produto.contador + 1 # é um atributo de instancia, mas nao é recebido como parametro. Não é necessario
        # que todos sejam recebidos, uma vez que ele possui uma logica diferente, que se auto incrementa.
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor) # R:2415.0
print(p2.valor) # R:4725.0

# OBS: Não precisa criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # R: Acesso correto de um atributo de classe
print(p1.imposto) # R: Acesso possível, mas incoreto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python são chamados de
# atributos estáticos.

# Atributos Dinâmicos -> Um atributo de instancia que pode ser criado em tempo de execução.

# OBS O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg' # Na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')
# R: AttributeError: 'Produto' object has no attribute 'peso'

# Deletando atributos

print(p1.__dict__) # R: {'id': 1, 'nome': 'Playstation 4', 'descricao': 'Video Game', 'valor': 2415.0}
print(p2.__dict__) # R: {'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia', 'valor': 6.2895, 'peso': '5kg'}

del p2.peso
print(p2.__dict__) # R: {'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia', 'valor': 6.2895}
del p2.valor
print(p2.__dict__) # R: {'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia'}
del p2.descricao
print(p2.__dict__) # R: {'id': 2, 'nome': 'Arroz'}


POO - Métodos

- Métodos (Funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no
sistema.

Em Python, divide-se os métodos em 2 grupos: Métodos de instância e Métodos de Classe.

# Metodos de instância

# O método dunder init __init__ é um método especial chamado de construtor e sua função é contruir o objeto a partir da
classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

ATENÇÂO Por mais que seja possivel criar proprias funcoes utilizando dunder, não é aconselhado. O Python possui varios
métodos com esta forma de nomenclatura e pode ser que faça com que mude o comportamento dessas funções mágicas internas
da linguagem. Então, evite ao máximo. De preferência nunca o faça.

# Métodos sõ escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.

p1 = Produto('Playstation 4', 'Video Game', 2300)
print(p1.desconto(90))

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')


print(user1.nome_completo())
print(Usuario.nome_completo(user1))

------------------------------------------------------------------
from passlib.hash import pbkdf2_sha256 as cryp
# Este pacote, está usando um tipo de criptografia chamado sha256 que é extremamente poderoso.
class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        # Esta sendo usado a funcao hash, abrindo qual parametro/string que quer que seja encriptado (senha)
        # e passando dois parâmetros extras que vai definir quão forte vai ser a senha. round (embaralhamento) 200_000x
        # salt_size é o tamanho da outra parte texto que seja juntada para encriptografar

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

nome = input('informe o nome: ')
sobrenome = input('informe o sobrenome: ')
email = input('informe o email: ')
senha = input('informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print(f'Bem vindo {Usuario.nome_completo(user).title()}. Usuario criado com sucesso!')
else:
    print('Senha nao confere...')
    exit(1)

while True:
    senha = input('Informe a senha para acesso: ')
    if user.checa_senha(senha):
        print('Acesso permitido')
        break
    else:
        print('Acesso negado, senha incorreta!')
print(f'Senha User Criptografada: {user._Usuario__senha}') # Acesso errado


# Métodos de classe em Python são conhecidos como Métodos Estáticos em outras linguagens.


# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
Usuario.conta_usuarios() # Forma correta, acesso via nome de classe
user.conta_usuarios() # Possivel, ma nao correta, acesso via instancia da classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
print(user._Usuario__gera_usuario())


"""
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem))/100

from passlib.hash import pbkdf2_sha256 as cryp
# Este pacote, está usando um tipo de criptografia chamado sha256 que é extremamente poderoso.
class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')
    # cls é a propria classe. Uma convenção usada no Python. igual a Usuario.contador

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador +1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        # Esta sendo usado a funcao hash, abrindo qual parametro/string que quer que seja encriptado (senha)
        # e passando dois parâmetros extras que vai definir quão forte vai ser a senha. round (embaralhamento) 200_000x
        # salt_size é o tamanho da outra parte texto que seja juntada para encriptografar
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]

# Método Estático

print(Usuario.contador) # R: 0
print(Usuario.definicao()) # R: UXR344
user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
print(user.contador) # R: 1
print(user.definicao()) # R: UXR344


