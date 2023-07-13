"""
Cada módulo consiste em entidades (como um livro consiste em capítulos).
Essas entidades podem ser funções, variáveis, constantes, classes e objetos.
Se você sabe como acessar um determinado módulo, pode fazer uso de qualquer
uma das entidades que ele armazena.
"""


### como importar
# import math
# import sys
#
# import math, sys




# ### como chamar entidade
# import math
# print(math.sin(math.pi/2))




# ### dois "sin"s diferente
# import math
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
# pi = 3.14
# print(sin(pi/2))
# print(math.sin(math.pi/2))




# ### modulo com entity/entities
# from math import pi
# print(pi)
#
# from math import sin, pi
# print(sin(pi/2))



# ### # sopreposicao de funcao
# from math import sin, pi
#
# print(sin(pi / 2))
# pi = 3.14
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
# print(sin(pi / 2))




# ### import tudo -- you may not be able to avoid name conflicts.
# from module import *




# ###Aliasing
# import math as m
#
# print(m.sin(m.pi / 2))

# from math import pi as PI, sin as sine
#
# print(sine(PI / 2))



########    Observacoes:  ###############

# #assim é melhor:
# import mod2
# import mod3
# import mod4
#
# #do que:
# import mod2, mod3, mod4




# não é recomendada devido ao perigo de causar
# conflitos com nomes derivados da importação do namespace do código:

# from module import my_function, my_data
#
# result = my_function(my_data)











