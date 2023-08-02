"""
Módulo Random e o que são modulos?

- Em Python, módulos são outros arquivos Pythons.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatorio.

# OBS: Existem duas formas de se utilizar um módulo ou função deste
# Forma 01 - Importando todo o módulo
import random

# random() -> Gera um número pseudo-aleatório entre 0 e 1.

# Ao realizar o import de todo o módulo, todas as funçoes, atribulos, classes e propriedades que estiverem dentro do
#  módulo ficarão disponíveis (Ficarão em Memória). Caso voce saiba quais funções voce precisa utilizar deste módulo,
#  então esta não seria a forma ideal de utilização. Observa-se uma forma melhor na Forma 02.

print(random.random())

# Para utilizar a funçao random() do pacote random, coloca-se o nome do pacote e o nome da funçao, separados por ponto.
# OBS: Não confundir a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas uma
# função dentro do módulo random.

# Forma 02 - Importando uma função específica do módulo (Forma recomendada!)

from random import random

# No import acima, esta sendo falado: Do módulo random, importe a função random

for i in range(10):
    print(i, random())

# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(i, uniform(3, 7)) # 7 não é incluído

# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de aposta para mega-sena
for i in range(6):
    print(randint(1, 61), end=', ') # Começa em 1 e vai ate 60.
# R: 56, 15, 16, 23, 6, 36,

# choice() -> Mostra um valor aleatório entre um iterável.

from random import choice

jogadas = ['Pedra', 'Papel', 'Tesoura']

print(choice(jogadas)) # R: Papel
print(choice('Joao Ambrosio')) # R:A

"""
# Shuffle() -> Tem a função de embaralhar os dados
from random import shuffle\

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas) # R: ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
shuffle(cartas)
print(cartas) # R: ['K', '5', 'Q', '2', '4', 'A', 'J', '3', '7', '6']
print(cartas.pop(0)) # R: K
print(cartas) # R: ['5', 'Q', '2', '4', 'A', 'J', '3', '7', '6']
