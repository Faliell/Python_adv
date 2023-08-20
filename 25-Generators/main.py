""" Um gerador Python é um pedaço de código especializado capaz de
produzir uma série de valores e controlar o processo de iteração.
É por isso que os geradores são frequentemente chamados iteradores e,
embora alguns possam encontrar uma distinção muito sutil entre esses dois"""


"""exemplo"""


for i in range(5):
    print(i)


""" O protocolo iterador é uma maneira pela qual um objeto deve se comportar
 de acordo com as regras impostas pelo contexto das instruções for e in.
  Um objeto em conformidade com o protocolo do iterador é chamado de iterador."""


""" Um iterador deve fornecer dois métodos:

__iter__() que deve retornar o próprio objeto e que é invocado uma vez
(é necessário para o Python iniciar a iteração com sucesso)
 
__next__() que pretende retornar o próximo valor
(primeiro, segundo e assim por diante) da série desejada
– será invocado pelas instruções for/in para passar pela próxima iteração;
se não houver mais valores a serem fornecidos, o método deve gerar a exceção
StopIteration.
"""
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)


""" yield """


""" Você pode pensar na palavra-chave yield como uma irmã mais inteligente
da instrução return, com uma diferença essencial."""


""" Só retorna uma vez"""


def fun(n):
    for i in range(n):
        return i


""" transforma a função em um gerador """


def fun(n):
    for i in range(n):
        yield i


""" Todos os valores das variáveis são congelados, e aguardam a próxima invocação,
 quando a execução é retomada (não retirada do zero, como após o retorno).

Há uma limitação importante: tal função não deve ser invocada explicitamente
porque – na verdade – não é mais uma função; é um objeto gerador."""


""" Construir um gerador """


def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)


""" com potencia de 2 """


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)


""" dentro de list comprehensions"""


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]
print(t)


""" transformando em lista """


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(3))
print(t)


""" com in """


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for i in range(20):
    if i in powers_of_2(4):
        print(i)


""" Fibonancci """


def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n


fibs = list(fibonacci(10))
print(fibs)


""" Mais sobre compreensões de lista """


""" relembrando """


list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)


""" expressão condicional – uma forma de selecionar um dos dois valores
 diferentes com base no resultado de uma expressão booleana."""


the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)


""" o mesmo somente com list comprehension """


the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)


""" transformar qualquer compreensão de lista em um gerador """

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()


""" Como provar a diferença? use len(), geradores não tem len """


""" 
Nota: a mesma aparência da saída não significa que ambos os loops
funcionem da mesma maneira. No primeiro loop, a lista é criada (e iterada)
como um todo – ela realmente existe quando o loop está sendo executado.

No segundo loop, não há nenhuma lista – há apenas valores subseqüentes
produzidos pelo gerador, um a um.
"""


for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

