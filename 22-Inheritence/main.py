""" Defirnir __str__"""


class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


sun = Star("Sun", "Milky Way")
print(sun)


"""A herança é uma prática comum (na programação de objetos)
 de passar atributos e métodos da superclasse (definida e existente)
  para uma classe recém-criada, chamada de subclasse."""


"""Um exemplo muito simples de herança em dois níveis é apresentado aqui:"""


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


"""issubclass()"""


print(issubclass(Vehicle, LandVehicle))
print(issubclass(LandVehicle, Vehicle))



"""Mais elaborado"""
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()


"""isinstance()
isinstance(objectName, ClassName)
"""


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()


"""
Operador is
object_one is object_two

O operador is verifica se duas variáveis (object_one e object_two)
se referem ao mesmo objeto.

Não se esqueça de que as variáveis não armazenam os próprios objetos,
mas apenas os manipuladores que apontam para a memória interna do Python.
"""


class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)


"""métodos herdados"""

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)


"""A função super() cria um contexto no qual você não precisa
 (aliás, não deve) passar o argumento self para o método que
  está sendo invocado – por isso é possível ativar o construtor
   da superclasse usando apenas um argumento."""


class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)


"""com variáveis de classe"""
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)


"""com variáveis de instância"""


class Super1:
    def __init__(self):
        self.supVar = 11


class Sub(Super1):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()


"""Quando você tenta acessar a entidade de qualquer objeto,
 o Python tentará (nesta ordem):

-encontre-o dentro do próprio objeto;
-encontre-o em todas as classes envolvidas na linha de herança
 do objeto de baixo para cima;"""


"""three-level inheritance line"""


class Level1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())


"""Herança múltipla"""


class SuperA:
    var_a = 10

    def fun_a(self):
        return 11


class SuperB:
    var_b = 20

    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())


"""overriding"""


class Level1:
    var = 100

    def fun(self):
        return 101


class Level2(Level1):
    var = 200

    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())


"""Podemos dizer que Python procura por componentes de objeto na seguinte ordem:

-dentro do próprio objeto;
-em suas superclasses, de baixo para cima;
-se houver mais de uma classe em um determinado caminho de herança,
 o Python as examinará da esquerda para a direita."""


class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

# class Sub(Right,Left,):
class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())


"""a situação em que a subclasse é capaz de modificar o comportamento
 de sua superclasse (como no exemplo) é chamada de polimorfismo."""

"""O método, redefinido em qualquer uma das superclasses, alterando
 assim o comportamento da superclasse, é denominado virtual."""

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()