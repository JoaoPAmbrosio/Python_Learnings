"""
Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java

Utilizamos o break para sair de loops de maneira projetada.

# Exemplo 01
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("sai do loop")

"""
# Exemplo 02
vezes = 0
while True:
    comando = input("Digite 'sair' para sair: ")
    vezes += 1
    if comando == "sair":
        print(f'voce demorou {vezes} vezes para sair do loop!')
        break
    else:
        print("voce ainda está no loop ")
