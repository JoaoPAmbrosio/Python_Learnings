"""
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também
como tipo vazio, porém, falar que é um tipo sem tipo é mais aproprieado.

OBS: O tipo None é SEMPRE especificado com a primeira letra maiúscula.
Certo: None
Errado: none

Quando Utilizar?
- Pode-ser utilizar None quando criar uma variável e inicializá-la com um tipo sem tipo, antes
de receber um valor final.

OBS: O tipo None em Python é SEMPRE considerado como False

numeros = None
print(numeros)
print(type(numeros))
None
<class 'NoneType'>

numeros = 1.44, 1.34, 5.67
print(numeros)
print(type(numeros))
(1.44, 1.34, 5.67)
<class 'tuple'>

Em Python, quando uma função não retorna nenhum valor, o retorno é None
"""
