""" Também pode chamar de uma função anônima """

""" lambda parameters: expression """

""" Essa cláusula retorna o valor da expressão ao levar em consideração
o valor atual do argumento lambda atual."""


two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


""" exemplo de utilidade"""


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)


""" Com Lambda """


def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')


print_function([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)


""" Map """


""" map(function, list)
A função map() aplica a função passada por seu primeiro argumento a todos
os elementos de seu segundo argumento e retorna um iterador que fornece
todos os resultados subsequentes da função."""


list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()


""" filter() """


""" espera o mesmo tipo de argumento que map(), mas faz algo diferente:
– ele filtra seu segundo argumento enquanto é guiado por direções que fluem
da função especificada como o primeiro argumento (a função é invocada para
cada elemento da lista, assim como em map ()).

Os elementos que retornam True da função passam no filtro – os demais
 são rejeitados."""


from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)


"""closures"""


""" fechamento é uma técnica que permite o armazenamento de valores,
 apesar do fato de que o contexto em que foram criados não existe mais."""


def outer(par):
    loc = par


var = 1
outer(var)

print(var)
# gera erro:
# print(loc)


""" A função retornada durante a invocação de outer() é um closure."""


def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())


""" é totalmente possível declarar um fechamento equipado com
 um número arbitrário de parâmetros"""


def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))


""" PEP 8, o Guia de estilo para código Python, recomenda que lambdas
não sejam atribuídos a variáveis, mas sim definidos como funções."""













