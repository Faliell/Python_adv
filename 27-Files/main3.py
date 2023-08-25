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


""" 
como escrever uma matriz de bytes em um arquivo binário,
queremos escrever uma cópia um-para-um do conteúdo da memória física, byte por byte. 
 """

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


""" 
Como ler bytes de um stream 

readinto()
"""

"""
-o método retorna o número de bytes lidos com sucesso;
-o método tenta preencher todo o espaço disponível dentro do seu argumento;
se houver mais dados no arquivo do que espaço no argumento, a operação de
leitura será interrompida antes do final do arquivo; caso contrário,
o resultado do método pode indicar que a matriz de bytes foi preenchida
apenas fragmentariamente
"""


from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


""" Alternativa de ler o conteúdo de um arquivo binário: read()."""


try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read(5))
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

"""
Observação: os primeiros cinco bytes do arquivo foram lidos pelo código
– os próximos cinco ainda aguardam processamento.
"""


""" Copying files """


"""
o objetivo não é substituir melhor comandos como copy (MS Windows)
ou cp (Unix/Linux), mas ver uma forma possível de criar uma ferramenta
de trabalho, mesmo que ninguém queira usá-la. 
"""

from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

print(total, 'byte(s) succesfully written')
src.close()
dst.close()