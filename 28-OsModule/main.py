""" Obtendo informações sobre o sistema operacional """


""" a função uname retorna um objeto contendo informações sobre o sistema operacional """


import platform
import os
# print(os.uname()) # em unix

print(platform.uname()) #windows


""" 
os.name
    posix — you'll get this name if you use Unix;
    nt — you'll get this name if you use Windows;
    java — you'll get this name if your code is written in Jython."""
print(os.name)


""" criar diretorios"""


""" 
my_first_directory — este é um caminho relativo que criará o
diretório my_first_directory no diretório de trabalho atual;

./my_first_directory — este é um caminho relativo que aponta explicitamente
para o diretório de trabalho atual. Tem o mesmo efeito do caminho acima;

../my_first_directory — este é um caminho relativo que criará o diretório
my_first_directory no diretório pai do diretório de trabalho atual;

/python/my_first_directory — este é o caminho absoluto que criará o diretório
my_first_directory, que por sua vez está no diretório python no diretório raiz.
"""

os.mkdir("my_first_directory")
print(os.listdir())


""" A função listdir retorna uma lista contendo os nomes dos arquivos e diretórios
 que estão no caminho passado como argumento.

Se nenhum argumento for passado para ele, o diretório de trabalho atual será usado

"""