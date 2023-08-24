""" Abrir arquivos"""

""" texto simples """

stream = open('file.txt', 'rt', encoding='utf-8')

import os

stream = open('file.txt', "rt")
content = stream.read()
print(content)

try:
    counter = 0
    stream = open('file.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", os.strerror(e.errno))

""" Lembre-se: ler um arquivo de terabytes usando esse método pode
corromper seu sistema operacional. """

""" Função read(), invocada sem nenhum argumento ou com um argumento
avaliado como None """

try:
    counter = 0
    stream = open('file.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", os.strerror(e.errno))

""" readlines() """

""" 
quando invocado sem argumentos, tenta ler todo o conteúdo do arquivo e
retorna uma lista de strings, um elemento por linha do arquivo.

O tamanho máximo do buffer de entrada aceito é passado ao método como
seu argumento.

O argumento especifica o número máximo de bytes a serem lidos do arquivo
"""

stream = open("file.txt")
# print(stream.readlines())

print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()

""" mais elaborado """

try:
    ccnt = lcnt = 0
    s = open('file.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", os.strerror(e.errno))

""" o objeto retornado pelo open()  é uma instância da classe iterável """

try:
    ccnt = lcnt = 0
    for line in open('file.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", os.strerror(e.errno))

""" 
write()
 
espera apenas um argumento – uma string que será transferida para um arquivo aberto
"""

""" exemplo escrevendo por char """


# try:
#     file = open('newtext.txt', 'wt')  # A new file (newtext.txt) is created.
#     for i in range(10):
#         s = "line #" + str(i + 1) + "\n"
#         for char in s:
#             file.write(char)
#     file.close()
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))


""" outro exemplo escrevendo a linha"""


try:
    file = open('newtext.txt', 'wt')
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("I/O error occurred: ", os.strerror(e.errno))


""" 
Nota: você pode usar o mesmo método para gravar no fluxo stderr
("standard error"), mas não tente abri-lo, pois ele está sempre
aberto implicitamente.

Por exemplo, se você quiser enviar uma string de mensagem para stderr para
distingui-la da saída normal do programa, ela pode ter esta aparência:
"""

import sys
sys.stderr.write("Error message")

