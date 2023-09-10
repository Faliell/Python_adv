"""
Quando Python acha um erro:
-ele interrompe o seu programa;
-ele cria um tipo especial de dados, chamado exceção.
"""

# Momento que chama except
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")

#####################################
# # Qual o erro?
#
# # exemplo 1:
#
# try:
#     print("Let's try to do this")
#     print("#"[2])
#     print("We succeeded!")
# except:
#     print("We failed")
# print("We're done")
#
# # exemplo 2:
#
# try:
#     print("alpha"[1/0])
# except ZeroDivisionError:
#     print("zero")
# except IndexError:
#     print("index")
# except:
#     print("some")
###########################################

"""
as except ramificações são pesquisadas na mesma ordem em que aparecem no código;
 
você não deve usar mais de um branch exceto com um determinado nome de exceção;

o número de except ramificações diferentes é arbitrário - a única condição
é que se você usar try, você deve colocar pelo menos uma except (nomeada ou não)
depois dela;

a except palavra-chave não deve ser usada sem um precedente try;

se alguma das except ramificações for executada, nenhuma outra ramificação
será visitada;

se nenhuma das except ramificações especificadas corresponder à exceção
levantada, a exceção permanecerá sem tratamento;

se except existir uma ramificação sem nome (uma sem nome de exceção), ela
deverá ser especificada como a última.
"""

#######################################################


""" O Python 3 define 63 exceções internas e todas elas formam uma hierarquia
em forma de árvore, embora a árvore seja um pouco estranha,
pois sua raiz está localizada no topo. """


def treeClass(cls, ind=0):
    print('-' * ind, cls.__name__)

    for i in cls.__subclasses__():
        treeClass(i, ind + 3)


print("Hierarchy for Built-in exceptions is : ")
# treeClass(BaseException)


####################################################

""" 
cada exceção levantada cai no primeiro ramo correspondente ;
o ramo correspondente não precisa especificar exatamente a mesma exceção 
- é suficiente que a exceção seja mais geral (mais abstrata) do que a levantada.

A ordem dos ramos é importante!
Não coloque exceções mais gerais antes das mais concretas;
"""

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")


################################################


""" Se quiser tratar duas ou mais exceções da mesma maneira,
você pode usar a seguinte sintaxe:"""

try:
    print(1/0)
except (ZeroDivisionError, ValueError):
    print("Erro: Houve um problema com a operação.")


##############################################

""" 
raise - força o erro

Apenas raise: este tipo de instrução de raise pode ser usado apenas dentro
 da ramificação except
"""


def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")





def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")



### assert

"""1- Avalia a expressão;
2- se a expressão for avaliada como True, ou um valor numérico diferente de zero,
ou uma string não vazia, ou qualquer outro valor diferente de None,
ela não fará mais nada;
-3caso contrário, automaticamente e imediatamente gera uma exceção
chamada AssertionError (neste caso, dizemos que a asserção falhou)"""

import math
#
# x = float(input("Enter a number: "))
# assert x >= 0.0
# x = math.sqrt(x)
# print(x)


### Desafio1:

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("zero")
# except ArithmeticError:
#     print("arith")
# except:
#     print("some")


### Desafio2:

# try:
#     print(1/0)
# except ArithmeticError:
#     print("arith")
# except ZeroDivisionError:
#     print("zero")
# except:
#     print("some")


### Desafio3:

# def foo(x):
#     assert x
#     return 1 / x
#
#
# try:
#     print(foo(0))
# except ZeroDivisionError:
#     print("zero")
# except:
#     print("some")



