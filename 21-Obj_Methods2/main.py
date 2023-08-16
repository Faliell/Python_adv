"""Todos esses meios permitem ao programador Python realizar duas
importantes atividades específicas para muitas linguagens OOP. São eles:

- introspeção: a capacidade de um programa examinar o tipo
 ou as propriedades de um objeto em tempo de execução

- reflexão: que vai um passo além, e é a capacidade de um
 programa manipular os valores, propriedades e/ou funções de um objeto
  em tempo de execução."""


class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)


"""1. Um método é uma função embutida dentro de uma classe.
O primeiro (ou único) parâmetro de cada método geralmente é denominado self,
que é projetado para identificar o objeto para o qual o método é invocado
para acessar as propriedades do objeto ou invocar seus métodos.


2. Se uma classe contém um construtor (um método chamado __init__),
ela não pode retornar nenhum valor e não pode ser invocada diretamente.


3. Todas as classes (mas não os objetos) contêm uma propriedade denominada __name__,
que armazena o nome da classe. Além disso, uma propriedade denominada
__module__ armazena o nome do módulo no qual a classe foi declarada,
enquanto a propriedade denominada __bases__ é uma tupla contendo as superclasses
de uma classe."""
