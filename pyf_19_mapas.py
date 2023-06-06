"""
Mapas -> Conhecidos em Pythons como Dicinonários

Dicionários em Python sao representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}
# Interar sonbre dicionários
for chave in receita:
    print(chave)
# jan \n fev \n mar
for chave in receita:
    print(receita[chave])
# 100 \n 250 \n 400

print(receita.keys())
for chave in receita.keys():
    print(receita[chave])

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
# print(receita.keys()) # dict_keys(['jan', 'fev', 'mar'])
# print(receita.values()) # dict_values([100, 250, 400])

for valor in receita.values():
    print(valor) # 100 \n 250 \n 400

print(receita.items())
# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
