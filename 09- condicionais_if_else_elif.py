"""
Estruturas condicionais
if, else, elif
"""
"""
# Estrutura condicional if, else em C

if(idade < 18){
    printf("Menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos");
}else{
    printf("Maior de idade");
}

# Estrutura condicional if, else em Java

if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("Maior de idade");
}
"""
idade = int(input('Qual sua idade?\n'))

if idade < 18:
    print(f'Menor de idade.\nVoce nasceu em {2023-idade}.')
elif idade == 18:
    print(f'Tem 18 anos.\nVoce nasceu em {2023-idade}.')
else:
    print(f'Maior de idade.\nVoce nasceu em {2023-idade}.')
