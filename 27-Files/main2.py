""" Abrir arquivos"""

""" texto simples """

stream = open('file.txt', 'rt', encoding='utf-8')
print(stream.read())

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



""" Função read(), invocada sem nenhum argumento ou com um argumento
avaliado como None """

""" Lembre-se: ler um arquivo de terabytes usando esse método pode
corromper seu sistema operacional. """

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


""" readline()

O método tenta ler uma linha completa de texto do arquivo e a retorna como
uma string em caso de sucesso. Caso contrário, retorna uma string vazia.

Pode receber um parâmetro size, que especifica o número máximo de caracteres
a serem lidos na linha atual. Ele lerá até atingir o número de caracteres
especificado ou até atingir o final da linha, o que ocorrer primeiro.
"""

try:
    ccnt = lcnt = 0
    s = open('file.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", os.strerror(e.errno))



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


""" 
O objeto retornado pelo open()  é uma instância da classe iterável

Você pode esperar que o objeto seja invocado automaticamente close() 
quando qualquer leitura do arquivo atingir o final do arquivo.
"""

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
 
Espera apenas um argumento – uma string que será transferida para um arquivo aberto

O modo aberto w garante que o arquivo será criado do zero , mesmo que exista
e contenha dados.
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
sys.stderr.write("Error message 123")

