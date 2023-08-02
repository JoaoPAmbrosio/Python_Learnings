"""
Módulos customizados

Como módulos Python são arquivos Python, então TODOS os arquivos criados são módulos Python prontos para serem utilizados

# Importando uma função específica do módulo
from pyf_28_funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

import pyf_28_funcoes_com_parametro as fcp

print(fcp.lista)
print(fcp.soma_impares(fcp.lista))

"""
from pyf_39_map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
