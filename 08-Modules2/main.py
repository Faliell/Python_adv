import math

# dir() ver entidades do modulo
print(dir(math))

# expoente
print(math.pow(2, 2))

x = 2.1
y = 3.9
# aredonda para cima
print(math.ceil(x))
# aredonda para baixo
print(math.floor(y))
# remove parte decimal
print(math.trunc(x))

import random

# de 0.0 a 0.999..
print(random.random())

### Seed

"""O parâmetro a é a semente, que pode ser um número inteiro ou
 um objeto hashável (como uma string). Se a não for especificado ou for None,
  a função utilizará um valor de semente baseado na hora atual do sistema,
   tornando os números aleatórios diferentes a cada execução do programa."""

random.seed(42) # determina

"""Agora, ao usar a função de geração de números aleatórios,
obteremos a mesma sequência a cada execução. """
print(random.random())   # Saída: 0.6394267984578837
print(random.random())   # Saída: 0.025010755222666936
print(random.random())   # Saída: 0.27502931836911926

random.seed()

### randrange, randint
### random.randrange(start, stop, step)
### 2ºparametro não inclusivo
print(random.randrange(10))
print(random.randrange(0, 5))
print(random.randrange(0, 10, 2))
### 2ºparametro inclusivo
print(random.randint(0, 1))


### Choice, sample

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))



# Modulo Platform

import platform

platform.platform(aliased=False, terse=False)

""" aliased → quando definido como True (ou qualquer valor diferente de zero)
pode fazer com que a função apresente os nomes alternativos da camada
subjacente em vez dos comuns;
    terse → quando definido como True (ou qualquer valor diferente de zero),
pode convencer a função a apresentar uma forma mais resumida do resultado
(se possível)"""

print(platform.platform())
print(platform.platform(1))
print(platform.platform(0, 1))


### generic name of the processor
print(platform.machine())
### real processor name
print(platform.processor())
### generic OS name
print(platform.system())
### OS version
print(platform.version())
### Python implementation
print(platform.python_implementation())
### Python's version
print(platform.python_version_tuple())

### modulos index
### https://docs.python.org/3/py-modindex.html








