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
from random import randrange
random_num1 = randrange(10)  # Gera um número aleatório entre 0 e 9.
random_num2 = randrange(1, 11)  # Gera um número aleatório entre 1 e 10.
random_num3 = randrange(0, 100, 10)  # Gera um número aleatório entre 0 e 90 com um passo de 10.

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
%d
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
file.seek(offset, whence)

offset: É um valor inteiro que especifica a posição para onde você deseja
mover o cursor (em bytes). O valor positivo move o cursor para frente no arquivo,
e o valor negativo move o cursor para trás.

whence (opcional): É um valor que especifica de onde você deseja calcular o
deslocamento. Os valores possíveis são:
0 (padrão): Calcula o deslocamento em relação ao início do arquivo.
1: Calcula o deslocamento em relação à posição atual do cursor.
2: Calcula o deslocamento em relação ao final do arquivo.
"""


"""
errno.EEXIST - File exists
errno.EBADF - Bad file number
errno.EACCES - Permission denied
errno.ENOENT "No such file or directory"
"""


"""
argv
argv é usada com o módulo sys, para acessar argumentos passados a um
script ou programa a partir da linha de comando. 
retorna lista, os itens são sempre tratados como strings

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
# class A:
#     def a(self):
#         print('a')
#
# class B(A):  # dá erro de mro
#     def a(self):
#         print('b')
#
# class C(A, B):
#     def c(self):
#         self.a()
#
# c = C()
# c.c()
# print(C.mro())
###############################################


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
Operadores lógicos not, and, or
Operador de atribuição =
"""


"""
fabs() returns the float value of the absolute value.
floor() rounds a number down to the nearest integer
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


"""
Hierarquia
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

"""
sorted()   
Você pode usar com qualquer objeto iterável, não apenas listas.
Retorna uma nova lista e não modifica a lista original.
nova_lista = sorted(lista)

sort()
Disponível apenas para listas. Ele ordena a própria lista.
lista = [3, 1, 2, 4]
lista.sort()
"""

"""
join()
string_resultante = separador.join(iterável)
"""
# palavras = ["Python", "é", "uma", "linguagem"]
# print(" ".join(palavras))


"""
Quando você chama uma função com menos argumentos do que ela espera,
você pode gerar um TypeError, especificamente um TypeError do tipo "missing
positional argument" (argumento posicional ausente).
"""

"""
versão do pip:
pip --version
pip -V
"""

"""
em Bash:

"-" (Hífen Simples):
Usado para passar opções curtas ou abreviadas para um comando.
Geralmente, as opções com hífen simples são opções de uma letra ou configurações
curtas. -V -h

"--" (Hífen Duplo):
O hífen duplo é usado para passar opções longas e descritivas para um comando.
--version --help
"""


"""
".pyc" quando se trata de arquivos que armazenam o bytecode Python compilado.
"""

"""
When there is no __str__() method present and you print an object,
Python shows the object id in that way.
"""

"""
o bloco else em uma estrutura try/except é executado quando nenhuma exceção
é lançada no bloco
"""

"""
você pode usar um loop for para iterar por meio de uma string
"""
# minha_string = "Olá, mundo!"
#
# for caractere in minha_string:
#     print(caractere)


"""
If a function does not have the keyword return
the function will return the value None
The same happens if there is no value after the keyword return
"""


"""
sys.stdin: Esta é a corrente de entrada padrão (standard input). Ela está associada
ao teclado e é usada para receber dados de entrada a partir do usuário ou de
outros programas. Por exemplo, a função input() em Python lê dados do usuário
a partir de sys.stdin.

sys.stdout: Esta é a corrente de saída padrão (standard output). Ela está
associada ao monitor ou à tela e é usada para exibir dados de saída, como
resultados de programas. Por exemplo, a função print() em Python escreve dados
em sys.stdout.

sys.stderr: Esta é a corrente de erro padrão (standard error). Assim como
sys.stdout, ela está associada ao monitor e é usada para exibir mensagens
de erro e exceções.

Essas correntes são objetos da biblioteca sys e permitem a comunicação padrão 
entre o seu programa Python e o ambiente em que ele é executado. Você pode
redirecionar ou manipular essas correntes, se necessário, para realizar tarefas
específicas, como redirecionar a saída para um arquivo ou ler dados de uma fonte
diferente do teclado.
"""

"""
o módulo que suporta expressões regulares é chamado re
"""

"""
for x in open('file', 'rt'):
    print(x)
    
Le o arquivo linha por linha.
"""


"""
import platform
 
print(platform.platform())   # e.g. macOS-10.16-x86_64-i386-64bit
print(platform.processor())  # e.g. i386
print(platform.node())          # network name

"""

"""
"not" operator has the highest precedence,
followed by the "and" operator.
The "or" operator has the lowest precedence.
"""

"""
A função map pode aceitar mais de dois argumentos, mas os primeiros
dois são obrigatórios
map(função, iterável1, iterável2, ...)
Retorna um objeto de mapeamento, que é um iterador
"""

"""
class Test:
    def __init__(self, id):
        self.id = id
        id = 100  # This is a local variable of this method

x = Test(23)
print(x.id)  # 23
"""


"""
O else executa sempre após o while terminar, se tiver o break o
else não é executado
"""


"""
The Exception class contains a property named args and it is a: tuple
"""
# try:
#     raise ValueError()  # Sem mensagem de erro específica
# except ValueError as e:
#     print(e.args)  # Isso imprimirá uma tupla vazia ()


"""
readline():
A função readline() é usada para ler uma única linha de um arquivo.
Ela lê a próxima linha no arquivo toda vez que é chamada.
Retorna a linha lida como uma string, incluindo o caractere de nova
linha (\n) no final da linha.

readlines():
A função readlines() é usada para ler todas as linhas de um arquivo e
retorná-las como uma lista de strings.
Cada elemento da lista corresponde a uma linha do arquivo, incluindo o
caractere de nova linha (\n) no final de cada linha.
"""

""" em um dic str é diferente de int como key"""
# d = {}
# d[1] = 1
# d['1'] = 2
# d[1] += 1
#
# print(d)


"""
O método read() tem um parâmetro opcional.
Se for dado, esse número de caracteres é lido.
Se não for dado, é lido o ficheiro inteiro.
file.readline([tamanho])
O método readline() tem também um parâmetro opcional
para especificar o número de caracteres a serem lidos.
Mas ele só leria esse número de caracteres da
da primeira linha.
"""

"""
Esta pergunta é sobre a passagem de argumentos.
Há uma grande diferença entre passar um tipo de dados mutável ou imutável.
O inteiro imutável em x é copiado para p1
e a alteração de p1 não afecta x
A lista mutável em y é referenciada para p2
e a alteração de p2 afecta y
"""
# def func(p1, p2):
#     p1 = 1
#     p2[0] = 42
#
#
# x = 3
# y = [1, 2, 3]
#
# func(x, y)
#
# print(x, y[0])  # 3 42


"""
import x.z.f
se f é uma funcao vai dar erro, pq só pode chamar modulo com import
"""

"""
lista.insert(índice, elemento)
del frutas[1]

insert() insere um item numa determinada posição.
O primeiro argumento é o índice do elemento antes do qual inserir.
insert(0, 1) insere 1 antes do índice 0 (na frente da lista).
A palavra-chave del elimina o objeto dado.
Neste caso, x[1]
"""


"""
print('' in 'alphabet') # True
Uma string vazia é tratada como se
fosse uma parte (invisível) de cada string.
"""


"""
string.split()
O método split() sem passar nenhum argumento
dividirá a string nos seus espaços em branco e retornará uma lista das partes.
"""

"""
__eq__() é um método especial usado para definir a lógica de igualdade entre 
objetos de uma classe. Esse método é chamado quando você usa o operador
de igualdade == para comparar dois objetos de uma classe personalizada

def __eq__(self, other):
self se refere ao objeto em que o método é chamado (o objeto da instância atual).
other se refere ao objeto que está sendo comparado com o objeto atual.
"""

"""
String literals that are delimited by whitespace are automatically concatenated.
"""
#print('Peter' 'Wellert')  # PeterWellert

"""
__dict__
Atributos de Instância: Para objetos de instâncias de uma classe, o __dict__
contém pares chave-valor correspondentes aos atributos de instância do objeto.
Isso permite que você acesse e modifique os atributos diretamente através
do dicionário.
Atributos de Classe: Para classes, o __dict__ contém os atributos da classe,
incluindo variáveis de classe e métodos. Isso permite que você acesse e modifique
os atributos da classe diretamente através do dicionário.
"""

# print(-abs(3))  # -3


"""
listdir() never includes
the special entries . and ..
"""

"""
shuffle()
random.shuffle(minha_lista)
Ordena aleatoriamente a própria lista e não retorna uma nova lista
"""

"""
Com pip list obtém uma lista com todos os seus pacotes instalados.
Escolha um de seus pacotes e digite pip show package-name
"""

"""
index()
lista.index(valor, start, stop)
é usado para encontrar a primeira ocorrência de um valor específico dentro
de uma lista em Python. Ele retorna o índice da primeira ocorrência desse valor.
"""

"""
data = 'abbabadaadbbaccabc'
print(data.count('ab', 1))
O primeiro argumento é a subcadeia 'ab' que você deseja contar.
O segundo argumento é 1, o que significa que a contagem começará a
partir do índice 1 da string data.
"""

# foo = (1, 2, 3)
# foo.index(0)  # ValueError: tuple.index(x): x not in tuple


"""
Neste caso, a e b estão apontando para o mesmo objeto, então, se 
você modificar um deles, o outro também será modificado, porque ambos
se referem à mesma instância da classe A."""
# class A:
#
#     def __init__(self, v=2):
#         self.v = v
#
#     def set(self, v=1):
#         self.v += v
#         return self.v
#
#
# a = A()
# b = a
# b.set()
#
# print(a.v)


# b = bytearray(3)
# print(b)  # bytearray(b'\x00\x00\x00')


"""
set() é uma função que cria um objeto do tipo conjunto (set). Um conjunto
é uma coleção de elementos não ordenados e únicos.
"""
# data = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# print(len(data))


"""
O símbolo errno.ENOENT refere-se a um código de erro na programação
de computadores que significa "No such file or directory" (ficheiro ou
diretório inexistente).
"""


"""
O operador x << 1 está deslocando os bits de x para a esquerda em uma posição.
Em termos simples, isso é equivalente a multiplicar x por 2 elevado à primeira
potência. Assim, em cada iteração do loop, o valor de x é dobrado.

Aqui está o que acontece em cada iteração:

Primeira iteração: x era 1, depois x se torna 2 (1 << 1).
Segunda iteração: x era 2, depois x se torna 4 (2 << 1).
Terceira iteração: x era 4, depois x se torna 8 (4 << 1).
"""
# x = 1
# while x < 10:
#     print('*')
#     x = x << 1


"""
O operador xor bit a bit devolve 1 quando um operando é 1 e o outro é 0
Quando ambos os operandos são 0 ou ambos os operandos são 1, devolve 0
"""
# print(1 ^ 1)  # 0
# print(1 ^ 0)  # 1
# print(0 ^ 1)  # 1
# print(0 ^ 0)  # 0

"""
posso inicializar um global dentro da func
"""
# def func(x):
#     global y
#     y = x * x
#     return y
#
# func(2)
# print(y)  # 4


"""
id() é usada para obter a identificação (ou endereço de memória)
de um objeto

Um objeto é mutável e se criar dois novos objectos com os mesmos valores
eles continuarão a ser objectos diferentes e terão ids diferentes.
Uma string é imutável e se criar duas cadeias de caracteres com o mesmo valor
ambas apontarão para o mesmo objeto e, portanto, terão os mesmos ids.
"""


""" bloco try:"""
# try:
#     result = 1 / 0  # Tentando dividir por zero
# except (ZeroDivisionError, ArithmeticError) as e:
#     print(f"Ocorreu um erro: {e}")


"""
assert gera um  AssertionError se não acertar
"""


# data = [1, 2, 3, 4] + [1]
# print(data)  # [1, 2, 3, 4, 1]


# print(type(1J))  # <class 'complex'>
# print(type(1E1))  # <class 'float'>


# data = ()
# print(data.__len__())

# x = 2
# y = 1 + 1
# print(x is y)
# print(id(x), id(y))


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x[::2] = 10, 20, 30, 40, 50,  # 60 da erro
# print(x)
# x[1:2] = 5,5
# print(x)


# print(1 & 0)      # 0
# print(1 | 0)      # 1
# print(1 ^ 0)      # 1


"""
sys.path é uma lista com todas as pastas onde o Python procura por módulos
quando usas a palavra-chave import.
A primeira é sempre a pasta que contém o script que executaste.
"""

# list1 = ['Peter', 'Paul', 'Mary', 'Jane']
# list2 = ['Peter', 'Paul', 'Mary', 'Jane']
#
# print(list1 is not list2)  # True
# print(list1 != list2)  # False


# print('\n' in """
# """)  # True
# # A newline character is a part of every multi-line string.


"""
O dicionário pode ter diferentes tipos de dados como chave.
MAS se um inteiro e um float tiverem o mesmo valor,
o segundo valor substitui os primeiros valores.
E o primeiro índice continua a dar o nome.
"""
# data = {}
# data[1] = 1
# data['1'] = 2
# data[1.0] = 4
# print(data)  # {1: 4, '1': 2}


"""
Yes, a tuple can be the index of a dictionary
"""
# x = {(1, 2): 1, (2, 3): 2}
# print(x[1, 2])

# x= "a"
# print(bool(x))  # True


"""
writelines() é usado para escrever uma lista de strings em um objeto de arquivo.
Ele escreve cada string na lista como uma linha no arquivo, sem adicionar
automaticamente caracteres de quebra de linha entre as linhas. 

with open('arquivo.txt', 'w') as arquivo:
    linhas = ['Linha 1', 'Linha 2', 'Linha 3']
    arquivo.writelines(linhas)
Após a execução deste código, o arquivo 'arquivo.txt' conterá as linhas:

Linha 1Linha 2Linha 3
"""


# print(not 0)  # True
# print(not 23)  # False
# print(not '')  # True
# print(not 'Peter')  # False
# print(not None)  # True

"""
intervalo [0.0, 1.0), o que significa que ele pode ser igual a 0.0,
mas nunca será igual a 1.0.
"""
# import random
# print(random.random())


# class A:
#     A = 23
#
#     def __init__(self):
#         self.a = 42
#
# x = A()
# print(hasattr(A, 'a'))  #False
# print(hasattr(x, 'A'))  #True
# print(hasattr(x, 'a'))  #True



# class Failure(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return "out of order"
#
#
# try:
#     print("turn on")
#     raise Failure("crash")
# except Failure as problem:
#     print(problem)
# else:
#     print("success")

"""
class Failure(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message  # Retorna a mensagem definida ao invés de "out of order"
"""


"""
Closure

def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

# Criar uma função que multiplica por 2
dobro = multiplicador(2)
resultado = dobro(5)  # Isso retornará 10

# Criar uma função que multiplica por 3
triplo = multiplicador(3)
resultado = triplo(5)  # Isso retornará 15
"""
# def quote(quo):
#     def embed(str):
#         return quo + str + quo
#
#     return embed
#
#
# dblq = quote('"')
# print(dblq('Jane Doe'))


"""
o método read(1) em modo de leitura ("r") para ler de um arquivo,
o argumento 1 indica que você está solicitando a leitura de 1 byte,
o que, em termos gerais, corresponde a 1 caractere.
"""


"""
None + 1 dá errado
"""


# print(Hello, World!)  # SyntaxError: invalid syntax


"""
Sem a linha:
self.args = (msg,)
a solução seria: exex
O método __init__() da classe-mãe Exception é chamado com
msg + msg que é 'exex'
Mas a variável args do próprio objeto é atribuída a (msg,)
que é a tupla ('ex',)
e que é impressa quando o próprio objeto é impresso.
"""
# class Ex(Exception):
#     def __init__(self, msg):
#         Exception.__init__(self, msg + msg)
#         self.args = (msg,)
#
#
# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)


# print(list("azx"))  # ['a', 'z', 'x']

# print(int(0.8)) # 0
