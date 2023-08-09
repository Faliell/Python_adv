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

