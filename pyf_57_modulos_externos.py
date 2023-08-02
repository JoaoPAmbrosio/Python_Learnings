"""
Módulos externos

Utiliza-se o gerenciador de pacotes Python chamado pip - Python Installer Package

Conhece-se todos os pacotes externos python em: https://pypi.org/

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo
pip install nome-do-modulo

# Instalando o pacote colorama

pip install colorama

# Utilizando o pacote instalado

from colorama import init, Fore
init()
print(Fore.MAGENTA + 'Joao Ambrosio')
print(Fore.BLUE + 'Joao Ambrosio')
print(Fore.RED + 'Joao Ambrosio')
print(Fore.YELLOW + 'Joao Ambrosio')

# http://www.fpdf.org/
from fpdf import FPDF
pdf = FPDF('P', 'mm','A4')
pdf.add_page()
pdf.set_font('helvetica', 'B', 16)
pdf.cell(40, 10, '<h1>PDF with Python!</h1>')
pdf.output('teste.pdf')

# https://pypi.org/project/fpdf2/
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(txt='PDF with Python!')

pdf.output('teste.pdf')

"""

# https://pypi.org/project/fpdf2/
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(txt='PDF with Python!')
pdf.output('teste.pdf')