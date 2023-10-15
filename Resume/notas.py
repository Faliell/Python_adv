"""
A string is an immutable data type.
If you create a second string of the same value,
Python will created a reference to the same object.
Therefore those two strings will have the same identity.
"""



"""
isfile() 
It checks whether the passed argument is a file.
eg. print(os.path.isfile('data.txt'))
"""

# python aceita isso:
# if 10 > 1 < 10:
#     print(1)


"""
The "return" with no value will return None
"""

"""
The dir() function returns all properties
and methods of the specified object, without the values.

eg: 
import math
print(dir(math))
"""


"""
O método seed() não tem um valor de retorno definido, pelo que devolve None
"""


"""
__bases__ is a tuple which contains the direct superclasses.
"""

"""
w+ or w
You need the plus sign + to have reading and writing.
"""

"""
argv
lista, os itens são sempre tratados como strings
"""


"""
The exponentiation operator has an associativity from right to left
therefore the right one is executed first.

print(2 ** 3 ** 2 ** 1) 
"""

"""
def func():
    try:
        return 1
    finally:
        return 2


res = func()
print(res)  # 2
"""


"""
print('Al' * 2 <= 'Alan')  # True
# 'AlAl' is less than 'Alan' because 'A' is less than 'a'.
"""


# ERROR:
# print(float("1, 3"))

"""
A função eval() em Python é usada para avaliar uma expressão Python
representada como uma string

x = 5
y = 10
expressao = "x + y"
resultado = eval(expressao)
print(resultado)  # Isso imprimirá 15
"""

"""
randrange(1, 5)
o segundo argumento do método  na biblioteca padrão Python não é inclusivo
"""

"""
randint(1, 5) the stop is inclusive.
"""


"""
The read() function reads the whole file
and returns a string.

The readlines() function also reads the whole file
and returns a list of the single lines.
And you can also iterate through the file object.
In each iteration you will get one line.
"""


"""
%-20s é usado para formatar uma string com um espaço total de 20 caracteres,
alinhando o texto à esquerda e preenchendo com espaços em branco à direita,
se necessário.
"""
# texto = "Exemplo"
# formatado = "%-20s bbb" % texto
# print(formatado)  # Exemplo              bbb

"""
4:  largura total do campo em que o valor será inserido.
Isso significa que o número será formatado para ocupar no mínimo 4 caracteres.
.1: O ponto e o número seguinte (neste caso, 1) indicam quantas casas decimais
devem ser exibidas após o ponto decimal no valor de ponto flutuante.
f: Indica que o valor a ser inserido é um número de ponto flutuante.
"""
# numero = 12.345
# formatado = "%4.1f" % numero
# print(formatado)

"""
será tratado como um número inteiro na string formatada
"""
# numero = 42
# formatado = "O número é: %d" % numero
# print(formatado)


"""
valores a serem inseridos na string são passados como uma tupla
(inteiro, ponto_flutuante) após o operador %.
"""

# inteiro = 42
# ponto_flutuante = 12.345
# frase = "Um inteiro: %d, ponto flutuante: %4.1f" % (inteiro, ponto_flutuante)
# print(frase)

"""
Modo	Descrição
'r'	Leitura (modo padrão). Abre o arquivo para leitura. Gera um erro
se o arquivo não existir.
'w'	Escrita. Abre o arquivo para escrita, truncando o arquivo (ou criando
um novo se não existir).
'a'	Anexação. Abre o arquivo para escrita, mas não trunca o arquivo,
mantendo o conteúdo existente. Se o arquivo não existir, ele é criado.
'x'	Criação exclusiva. Abre o arquivo para escrita, mas gera um erro se
o arquivo já existir.
'b'	Modo binário. Adicione 'b' ao modo para lidar com o arquivo em modo
binário (por exemplo, 'rb' ou 'wb').
't'	Modo texto (padrão). Adicione 't' ao modo para lidar com o arquivo em
modo de texto (por exemplo, 'rt' ou 'wt').
'+'	Leitura e escrita. Adicione '+' ao modo (por exemplo, 'r+' ou 'w+')
para permitir leitura e escrita no arquivo.
"""


"""
errno.EEXIST - File exists
errno.EBADF - Bad file number
errno.EACCES - Permission denied
"""


"""
terminal: python index.py Hello
from sys import argv
print(argv[1])
First the name of the variable is argv (argument vector).
And second the index 0 always holds the filename.
Index 1 holds the first argument from the command line.
"""


# lista = [4]
# print(lista[-1])  # 4

#######################################
# class A:
#     def a(self):
#         print('a')
#
# # class B(A)  dá erro de mro
# class B:
#     def a(self):
#         print('b')
#
# # class C(B, A):  # Like this the result would be: b
# class C(A, B):
#     def c(self):
#         self.a()
#
# c = C()
# c.c()  # a
# print(C.mro())
#################################


"""
Em Python, os utilizadores podem definir excepções personalizadas criando
uma nova classe.
Esta classe de exceção tem de ser derivada,
direta ou indiretamente, da classe Exception incorporada.
"""

"""
The scientific notation always returns a float
"""
# amount = +42E7
# print(type(amount))


"""
Parênteses ()
Operadores de potenciação **
Operadores unários + (positivo) e - (negativo)
Operadores de multiplicação *, divisão /, e divisão inteira //
Operador de módulo %
Operadores de adição + e subtração -
Operadores de comparação (por exemplo, <, <=, >, >=, ==, !=)
Operadores lógicos and, or, not
Operador de atribuição =
"""


"""
fabs() returns the float value of the absolute value.
floor() rounds a number down to the nearest integer
Those are the two you need here.
The others are of no use here:
fmod() returns the float value of the remainder.
ceil() rounds a number up to the nearest integer
frexp() returns the mantissa and the exponent.
"""
# import math
# print(math.floor(4.9))  # 4
# print(math.fabs(-4))    # 4.0
# print(math.frexp(4))    # (0.5, 3)
# print(math.fmod(7, 2))  # 1.0
# print(math.ceil(3.1))   # 4