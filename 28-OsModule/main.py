""" Obtendo informações sobre o sistema operacional """


"""
uname
A função retorna um objeto contendo informações sobre o sistema operacional

A função uname só funciona em alguns sistemas Unix. Se você usa Windows,
pode usar a função uname no módulo platform , que retorna um resultado semelhante. 
"""


import platform
import os
#print(os.uname()) # em unix

print(platform.uname()) #windows


""" 
O módulo "os" permite distinguir rapidamente o sistema operacional usando o
atributo "name"

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

#os.mkdir("my_first_directory")
print(os.listdir())


""" A função listdir retorna uma lista contendo os nomes dos arquivos e diretórios
 que estão no caminho passado como argumento.

Se nenhum argumento for passado para ele, o diretório de trabalho atual será usado

"""


""" 
Criação de diretório recursivo 

A função makedirs permite a criação recursiva de diretórios, o que significa
que todos os diretórios no caminho serão criados. 
"""


#os.makedirs("my_first_directory/my_second_directory")
#os.chdir("my_first_directory")
print(os.listdir())

""" Para mover entre diretórios, você pode usar uma função chamada chdir ,
que altera o diretório de trabalho atual para o caminho especificado."""


"""Where am I now? getcwd"""

#os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())


""" Excluindo diretórios em Python rmdir removedirs 

Se um dos diretórios não existir ou não estiver vazio, uma exceção será gerada.
"""


# os.mkdir("my_first_directory")
# print(os.listdir())
# os.rmdir("my_first_directory")
# print(os.listdir())
#
#
# os.makedirs("my_first_directory/my_second_directory")
# os.removedirs("my_first_directory/my_second_directory")
# print(os.listdir())


""" The system() function """


returned_value = os.system("mkdir my_first_directory")
print(returned_value)


os.system("ls /Users/fabioschapowal/Desktop/Python/Python_adv/28-OsModule/my_first_directory")
os.system("ls")

"""
os.system("ls /caminho/para/seu/diretorio")  # No Linux/macOS
# ou
os.system("dir C:\\caminho\\para\\seu\\diretorio")  # No Windows """


""" Dependendo do sistema, retorna um resultado diferente.
No Windows, retorna o valor retornado pelo shell após a execução do comando
fornecido, enquanto no Unix, retorna o status de saída do processo."""

