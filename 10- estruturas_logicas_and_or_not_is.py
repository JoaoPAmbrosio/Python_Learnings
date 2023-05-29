"""
Estruturas lógicas: And (e), or (ou), not (não), is (é);

Operadores unários:
    - not
    Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisam ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo
"""
ativo = True
logado = True
"""
if not ativo and logado:
    print(f'Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print(f'Bem-vindo usuário')
"""
if not ativo:
    print(f'Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print(f'Bem-vindo usuário')
print(ativo is False)

