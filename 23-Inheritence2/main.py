"""
- um veículo rastreado faz uma curva parando e se movendo em uma de suas
trilhas (isso é feito pelo método control_track(), que será implementado
posteriormente)
- um veículo com rodas gira quando suas rodas dianteiras giram (isso é feito
pelo método turn_front_wheels())
- o método turn()  utiliza o método adequado para cada veículo específico.
"""

import time

"""Sem herança"""

class TrackedVehicle:
    def control_track(left, stop):
        pass

    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)


class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass

    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)


"""Construindo herança"""


class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)




class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)


"""
Composição

Composição é o processo de compor um objeto usando outros objetos diferentes.

- A herança estende os recursos de uma classe adicionando novos componentes
e modificando os existentes; em outras palavras, a receita completa está
contida na própria classe e em todos os seus ancestrais; o objeto pega todos
os pertences da classe e faz uso deles;

- A composição projeta uma classe como um contêiner capaz de armazenar e usar
outros objetos (derivados de outras classes) onde cada um dos objetos implementa
uma parte do comportamento desejado da classe.
"""


class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)


"""Existem duas classes chamadas Tracks e Wheels – elas sabem como
controlar a direção do veículo. Existe também uma classe chamada Vehicle
que pode usar qualquer um dos "controllers" disponíveis (os dois já definidos,
ou quaisquer outros definidos no futuro) – o próprio "controller" é passado
para a classe durante a inicialização."""


"""
1-uma única classe de herança é sempre mais simples,
segura e fácil de entender e manter;

2-a herança múltipla é sempre arriscada, pois você tem muito mais
oportunidades de cometer um erro ao identificar essas partes das
superclasses que efetivamente influenciarão a nova classe;

3-herança múltipla pode tornar a substituição extremamente complicada;
além disso, usar a função super() torna-se ambíguo;

4-a herança múltipla viola o princípio da responsabilidade única
(mais detalhes aqui:
  https://en.wikipedia.org/wiki/Single_responsibility_principle),
pois cria uma nova classe de duas (ou mais) classes que nada sabem uma da outra;

5-é sujerido fortemente a herança múltipla como a última
de todas as soluções possíveis – se você realmente precisa das
diversas funcionalidades oferecidas por diferentes classes,
a composição pode ser uma alternativa melhor."""


"""Method Resolution Order (MRO)"""
"""
MRO, em geral, é uma maneira (você pode chamá-la de estratégia)
na qual uma linguagem de programação específica examina a parte superior
da hierarquia de uma classe para encontrar o método de que ela precisa atualmente.
"""


"""Exemplo simples"""


class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


"""Agora com uma modificação"""


class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):  # nesta linha
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


""" Agora com conflito"""


class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")

#
# class Bottom(Top, Middle):
#     def m_bottom(self):
#         print("bottom")


# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()


"""o problema do diamante"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()


"""outro exemplo"""


class Top:
    def m_top(self):
        print("top")


class MiddleLeft(Top):
    def m_middle(self):
        print("middle_left")


class MiddleRight(Top):
    def m_middle(self):
        print("middle_right")


# class Bottom(MiddleRight, MiddleLeft):
class Bottom(MiddleLeft, MiddleRight):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


"""Resumo"""


"""
1. Um método chamado __str__() é responsável por converter o conteúdo
 de um objeto em uma string (mais ou menos) legível. Você pode redefini-lo
  se quiser que seu objeto possa se apresentar de uma forma mais elegante.
  
2. Uma função chamada issubclass(Class_1, Class_2) é capaz de determinar
  se Class_1 for uma subclasse de Class_2.
 
3. Uma função chamada isinstance(Object, Class) verifica se um objeto
  vem de uma classe indicada.
 
4. Um operador chamado is verifica se duas variáveis se referem ao mesmo objeto.

5. Uma função sem parâmetros chamada super() retorna uma referência ao mais próximo
  superclasse da classe.
 
6. Métodos, bem como variáveis de instância e classe definidas em uma superclasse
  são automaticamente herdados por suas subclasses.
 
7. Para encontrar qualquer propriedade de objeto/classe,
 o Python a procura dentro de:

-o objeto em si;
-todas as classes envolvidas na linha de herança do objeto de baixo para cima;
-se houver mais de uma classe em um caminho de herança específico,
Python os examina da esquerda para a direita;
-se ambos os itens acima falharem, a exceção AttributeError será lançada.

8. Se alguma das subclasses definir um método/variável de classe/instância
variável de mesmo nome existente na superclasse, o novo nome
substitui qualquer uma das instâncias anteriores do nome.
"""

