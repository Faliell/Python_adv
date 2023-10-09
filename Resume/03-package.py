""" ver package_module e package_module2 """

import package_module

""" Uma nova subpasta apareceu - Seu nome é __pycache__ """


print(package_module.__counter)

from package_module2 import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))


""" Existe uma variável especial (na verdade uma lista) que armazena todos
os locais (pastas/diretórios) que são pesquisados para encontrar um módulo
que foi solicitado pela instrução de importação."""

from sys import path

path.append('..∖∖modules')

for p in path:
  print(p)