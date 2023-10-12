#!/usr/bin/env python3

"""
A linha que começa com #! tem muitos nomes - shabang, shebang, hashbang,
librabang ou hashpling. Do ponto de vista do Python, é apenas um comentário,
pois começa com #.
Para sistemas operacionais Unix e semelhantes a Unix (incluindo MacOS),
essa linha instrui o sistema operacional sobre como executar o conteúdo do
arquivo (em outras palavras, qual programa precisa ser iniciado para interpretar
o texto). Em alguns ambientes (especialmente aqueles conectados a servidores web)
a ausência dessa linha causará problemas;

* uma string (talvez uma multilinha) colocada antes de qualquer instrução do
módulo (incluindo importações) é chamada doc-string e deve explicar brevemente
o propósito e o conteúdo do módulo;
"""

print(__name__)
__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i + 1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
