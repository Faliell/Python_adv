""" Uma das classes especializadas que o Python usa para armazenar dados amorfos."""

"""
Dados amorfos são dados que não possuem forma ou formato específico
– são apenas uma série de bytes.

Deve haver um contêiner especial capaz de lidar com esses dados.

Python tem mais de um desses contêineres – um deles é um nome de classe
especializado bytearray – como o nome sugere, é um array contendo bytes (amorfos).
"""

"""
Se você deseja ter tal contêiner, por exemplo, para ler uma imagem bitmap
e processá-la de alguma forma, você precisa criá-lo explicitamente,
usando um dos construtores disponíveis.
"""
data = bytearray(10)

"""
são mutáveis, aceita len() e você pode acessar qualquer um de seus elementos
usando a indexação convencional.

Há uma limitação importante – você não deve definir nenhum elemento da matriz
de bytes com um valor que não seja um número inteiro (violar esta regra causará
uma exceção TypeError) e não tem permissão para atribuir um valor que não
venha do intervalo de 0 a 255 inclusive (ValueError).

Você pode tratar qualquer elemento da matriz de bytes como valores inteiros
"""

# data = bytearray(10)
#
# for i in range(len(data)):
#     data[i] = 10 - i
#
# for b in data:
#     print(hex(b))


""" como escrever uma matriz de bytes em um arquivo binário """

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
