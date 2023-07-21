import module

print(module.__counter)

"""Uma nova subpasta apareceu - Seu nome é __pycache__"""

from module2 import suml, prodl

from sys import path

path.append('..∖∖modules')

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

for p in path:
  print(p)

