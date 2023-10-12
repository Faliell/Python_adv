"""
A string is an immutable data type.
If you create a second string of the same value,
Python will created a reference to the same object.
Therefore those two strings will have the same identity.
"""

"""
randint() the stop is inclusive.
"""

"""
isfile() 
It checks whether the passed argument is a file.
eg. print(os.path.isfile('data.txt'))
"""

# python aceita isso:
if 10 > 1 == 10:
    print(1)


"""
The "return" with no value will return None
"""

"""
The dir() function returns all properties
and methods of the specified object, without the values.

eg: 
import math
print(dir(math))
"""


"""
The seed() method has no defined return value and therefore it returns None
"""


"""
__bases__ is a tuple which contains the direct superclasses.
"""

"""
w+ or w
You need the plus sign + to have reading and writing.
"""

"""
lista argv são sempre tratados como strings
"""


"""
The exponentiation operator has an associativity from right to left
therefore the right one is executed first.

print(2 ** 3 ** 2 ** 1) 
"""

"""
def func():
    try:
        return 1
    finally:
        return 2


res = func()
print(res)  # 2
"""


"""
print('Al' * 2 <= 'Alan')  # True
# 'AlAl' is less than 'Alan' because 'A' is less than 'a'.
"""