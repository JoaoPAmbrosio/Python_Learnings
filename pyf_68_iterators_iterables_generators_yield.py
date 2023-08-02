"""
Entendendo Iterators e Itarabels

Iterator ->
    - Um objeto que pode ter iterado
    - Um objeto que retorna um dado, sendo elemento por vez quando uma função next() é chamada;

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

nome = 'Joao'
numeros = [1, 2, 3, 4, 5]

[print(i) for i in iter(nome)]
[print(i) for i in iter(numeros)]


Criando sua propria versão de loop
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
meu_for('Joao Ambrosio')

Escrevendo um iterador customizado
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration
for n in Contador(1, 6):
    print(n, end='')
print('\n')
for n in range(1, 6):
    print(n, end='')


Geradores
-Geradores (Generators) são Iterators (Iteradores);
OBS: O contrario não é verdadeiro. Ou seja, nem todo iterador é um generador.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funçõies Geradoras)
---------------------------------------------------------------------------------
| Funções                             | Generator Functions                     |
---------------------------------------------------------------------------------
| utilizam return                     | utilizam yield                          |
---------------------------------------------------------------------------------
| retornam uma vez                    | podem utilizar o yield multiplas vezes  |
---------------------------------------------------------------------------------
| quando executada, retornam um valor | quando executada, retornam um generator |
---------------------------------------------------------------------------------

# Exemplo Função Geradora (Generator Funcion)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator
print(list(conta_ate(10)))

Teste de Memória com Generators

# Sequencia de Fibonacci
1, 1, 2, 3, 5, 8, 13,...

# Função usando lista (449MB de memória usada)
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Função usando geradores (3MB de memória usada)
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

# YIELD !!YIELD !!YIELD !!YIELD !!YIELD !!YIELD !!YIELD !!YIELD !!
# yield retorna o valor, sem sair da função como o return faz.

# Teste
print(list(fib_gen(10)))
for n in fib_gen(10):
    print(n)

Teste de Velocidade com Expressoes Geradras
def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()
print(ge1) # R: <generator object nums at 0x000001E9C6ECC040>
print(list(ge1)) # R: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Outra forma de generation expression sem yield
ge2 = (num for num in range(1, 10))
print(ge2) # R: <generator object <genexpr> at 0x000001E9C6DEFED0>
print(list(ge2)) # R: [1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
# Realizando o teste de velocidade
import time

gen_inicio = time.time()
print(sum(num for num in range(100000000))) # R: 4999999950000000
gen_tempo = time.time() - gen_inicio
print(f'Generator: {gen_tempo}') # R: Generator: 9.535670042037964

# List comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)])) # R: 4999999950000000
list_tempo = time.time() - list_inicio
print(f'List comprehension: {list_tempo}') # R: List comprehension: 20.524861097335815
