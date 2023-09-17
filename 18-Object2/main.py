"""Uma stack é um objeto projetado para armazenar dados usando o
modelo LIFO - Last In - First Out. A pilha geralmente realiza pelo menos duas
 operações, denominadas push() e pop()."""


# ## procedual:

stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

##############################################

"""object:
o nome do construtor é sempre __init__
tem que ter pelo menos um parâmetro (geralmente é chamado de self)"""


class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")


stack_object = Stack()  # Instantiating the object.


""" nome começando com dois sublinhados (__), ele se torna privado
É assim que o Python implementa o conceito de encapsulamento . """


class Stack:
    def __init__(self):
        self.stack_list = []
        # self.__stack_list = [] #Private


stack_object = Stack()
print(len(stack_object.stack_list))

##################################################

""" Ser acessíveis a todos os usuários da classe Esse componente é chamado
public , portanto você não pode começar seu nome com dois (ou mais) sublinhados.
Há mais um requisito: o nome não deve ter mais do que um sublinhado final ."""

# ## com as funções:


class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

""" Aqui, ambas as funções possuem um parâmetro nomeado self na primeira posição
da lista de parâmetros.
Todos os métodos devem ter este parâmetro. Ele desempenha a mesma função que
o primeiro parâmetro do construtor.
Permite que o método acesse entidades (propriedades e atividades/métodos)
realizadas pelo objeto real . Você não pode omitir isso. Cada vez que Python
invoca um método, ele envia implicitamente o objeto atual como primeiro argumento.
"""


""" Existem duas pilhas criadas a partir da mesma classe base .
Elas trabalham de forma independente . Você pode fazer mais deles se quiser."""

stack_object_1 = Stack()
stack_object_2 = Stack()


# ## Desafio: tente prever a saída

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print(funny_stack.pop())


###############################


"""Super Class"""


class AddingStack(Stack):
    pass


"""Python força você a invocar explicitamente o construtor de uma superclasse"""


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


##############################################


""" invocar qualquer método (incluindo construtores) de fora da classe nunca
exige que você coloque o "self" argumento na lista de argumentos - invocar um
método de dentro da classe exige o uso explícito do "self" argumento e deve
ser colocado em primeiro lugar na lista. """


class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


#######################################################

""" 
Modificar método:

def push(self, val):
    self.__sum += val
    Stack.push(self, val)
    
    
- temos que especificar o nome da superclasse; isso é necessário para
indicar claramente a classe que contém o método, para evitar confundi-lo
com qualquer outra função de mesmo nome;

- temos que especificar o objeto de destino e passá-lo como o primeiro
argumento (ele não é adicionado implicitamente à invocação neste contexto).


Obter valores dos atributos:

def get_sum(self):
    return self.__sum

"""

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())


