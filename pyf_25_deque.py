"""
Módulo Collections - Deque
Podemos dizer que o deque é uma lista de alta performance.
"""
# Importa
from collections import deque

# Criando deques

deq = deque('joao')
print(deq)

# Adicionando elementos no deque
deq.append('y') # Adiciona no final
print(deq)
deq.insert(4, 'G') # Adiciona no local desejado
print(deq)
deq.appendleft('k') # Adiciona no começo
print(deq)

# Remover elemento
print(deq.pop()) # Remove o ultimo elemento e o retorna
print(deq)
print(deq.popleft()) # Remove o primeiro elemento e o retorna
print(deq)
