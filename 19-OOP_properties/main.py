""" Instance variables
Essas variáveis pertencem a instâncias individuais (objetos) de uma
classe e armazenam informações específicas para cada instância."""


class ExampleClass:
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5  # acrescenta

### __dict__
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


### privado

class ExampleClass:
    def __init__(self, val=1):
        self.__first = val

    def set_second(self, val=2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

"""Quando o Python vê que você deseja adicionar uma variável de instância 
 a um objeto e você vai fazer isso dentro de qualquer um dos métodos do objeto,
 ele distorce a operação da seguinte maneira:

-coloca um nome de classe antes do seu nome.
-ele coloca um sublinhado adicional no início.

É por isso que __first se torna _ExampleClass__first."""

### acesso:
print(example_object_1._ExampleClass__first)

### Váriavels de classes

"""Uma variável de classe é uma propriedade que existe em apenas uma cópia
 e é armazenada fora de qualquer objeto."""


class ExampleClass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)


###

class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(3)
example_object_3 = ExampleClass(5)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)



### __dict__ para classe e objeto
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)



"""você não pode esperar que todos os objetos da mesma classe tenham os mesmos
 conjuntos de propriedades."""

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
# print(example_object.b)  #erro


### try except

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass

"""Python fornece uma função que é capaz de verificar com segurança se algum
objeto/classe contém uma propriedade especificada. A função é denominada hasattr
e espera que dois argumentos sejam passados para ela:

a classe ou o objeto que está sendo verificado;
o nome da propriedade cuja existência deve ser informada 
(nota: deve ser uma string contendo o nome do atributo, não apenas o nome)"""


class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)

### Com classe:

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))


### outro exemplo:

class ExampleClass:
    a = 1

    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))

