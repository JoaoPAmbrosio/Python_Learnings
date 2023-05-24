"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:
- Estiver em àspas simples -> 'uma string', '234', 'a', 'True', '42,3'
- Estiver em àspas duplas -> "uma string", "234", "a", "True", "42,3"
- Estiver em àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42,3'''

nome = 'Para o chamado "Joao Ambrosio" '
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina \"Jolie'
print(nome)
print(type(nome))
print(nome.title())
print(nome.split()) -> Transforma em uma lista de strings

#[ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12]
#['j', 'o', 'a', 'o', ' ', 'a', 'm', 'b', 'r', 'o', 's', 'i', 'o']
nome = 'joao ambrosio'
print(nome[0:4])     #Slice de string
print(nome[5:13])   #Slice de string

# [    0,        1     ]
# [ 'Joao', 'Ambrosio']
print(nome.split()[0])
print(nome.split()[1])

"""
#- Estiver em àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42,3"""

nome = 'joao ambrosio'
"""
Comece do primeiro elemento, vá atéo ultimo elemento e inverta
"""
print(nome[::])
print(nome[::-1])  # Inversão da String Pythônico

print(nome.upper().replace('O', 'A').title())

print(type(nome))

texto = 'socorram me subino onibus em marrocos'     #Palíndromo
print(texto)
print(texto[::-1])
