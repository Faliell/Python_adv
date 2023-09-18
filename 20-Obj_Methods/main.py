"""
 Um método é obrigado a ter pelo menos um parâmetro (não existem
 métodos sem parâmetros. Um método pode ser invocado sem um argumento,
 mas não declarado sem parâmetros).

 O primeiro (ou único) parâmetro é geralmente denominado self.

 Se for invocar um método, não deve passar o argumento para o
 self - parâmetro - o Python irá configurá-lo para você.
 """


class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()


"""Se quiser que o método aceite parâmetros diferentes de self, você deve:

- coloque-os depois selfna definição do método;
- entregá-los durante a invocação sem especificar self"""

class Classy:
    def method(self, par):
        print("method:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)


"""O parâmetro self é usado para obter acesso às variáveis de instância
 e classe do objeto."""


class Classy:
    varia = 2

    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()


"""O parâmetro self também é usado para invocar outros métodos de
 classe/objeto de dentro da classe."""


class Classy:

    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()


"""
Se você nomear um método como este: __init__,
não será um método regular – será um construtor.

Se uma classe tiver um construtor, ele será invocado automática
e implicitamente quando o objeto da classe for instanciado.
 
- é obrigado a ter o self parâmetro
- pode (mas não precisa) ter mais parâmetros
- pode ser usado para configurar o objeto
"""


class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)


""" O construtor:
- não pode retornar um valor, pois foi projetado para retornar um objeto
 recém-criado e nada mais;
- não pode ser invocado diretamente do objeto ou de dentro da classe """


"""Como __init__é um método, e um método é uma função, você pode fazer os
mesmos truques com construtores/métodos que faria com funções comuns."""


class Classy:
    def __init__(self, value=None):
        self.var = value


obj_1 = Classy("object")
obj_2 = Classy()

print(obj_1.var)
print(obj_2.var)


""" Um método cujo nome começa com __ é (parcialmente) oculto."""


class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()


"""
Cada classe Python e cada objeto Python são pré-equipados com um conjunto
de atributos úteis.
__dict__
"""


class Classy:
    varia = 1

    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)


"""
Outra propriedade interna: __name__, que é uma string.
Existe apenas dentro das classes.
Para encontrar a classe de um determinado objeto,
você pode usar uma função chamada type()

Observe que uma declaração como esta:

print(obj.__name__)

causará um erro.
"""


class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)


"""
__module__, armazena o nome do módulo que contém a definição da classe.

Qualquer módulo chamado __main__ na verdade não é um módulo,
mas o arquivo que está sendo executado no momento.
"""


class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)


"""__bases__ é uma tupla. A tupla contém classes (não nomes de classe)
 que são superclasses diretas para a classe."""


class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

print(Sub.__bases__)

"""
Observação: uma classe sem superclasses explícitas aponta para um objeto
 (uma classe Python predefinida) como seu ancestral direto.
 
Nota: apenas as classes possuem este atributo - os objetos não. 
 """

















