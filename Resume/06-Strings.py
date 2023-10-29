"""
Os computadores armazenam caracteres como números. Há mais de uma maneira
possível de codificar caracteres, mas apenas algumas delas ganharam popularidade
mundial e são comumente usadas em TI: são elas ASCII (usado principalmente para
codificar o alfabeto latino e alguns de seus derivados) e UNICODE
(capaz de codificar virtualmente todos os alfabetos sendo usados por humanos).

2. Um número correspondente a um caractere específico é chamado codepoint .

3. UNICODE utiliza diferentes formas de codificação quando se trata de armazenar
os caracteres em arquivos ou na memória do computador: duas delas são UCS-4 e UTF-8
(esta última é a mais comum porque desperdiça menos espaço de memória).

BOM (Byte Order Mark) é uma combinação especial de bits que anuncia
a codificação usada pelo conteúdo de um arquivo (por exemplo, UCS-4 ou UTF-8).
"""

""" 
Strings do Python são sequências imutáveis.

Exemplos de len:
"""
word = 'by'
print(len(word))

empty = ''
print(len(empty))

i_am = 'I\'m'
print(len(i_am))


"""
Podem ser concatenados usando o operador +
e replicados usando o operador *
também são aplicáveis para strings  += e *=

A capacidade de usar o mesmo operador contra tipos de dados completamente
diferentes (como números versus strings) é chamada de overloading 
"""

""" 
Multiline
/n invisivel  conta-  (\) não conta
 """
multiline = """Line #1
Line #2"""

print(len(multiline))

### conhecer o valor do ponto de código ASCII/UNICODE de um caractere específico
print(ord("a"))

### obter o caractere correspondente
print(chr(97))
"""
chr(ord(x)) == x
ord(chr(x)) == x
"""

### index
print("exemplo"[-1])

### iterar
the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

### Slices
alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

### in e not
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

"""
NÃO aceita del, append e insert
Python strings são imutáveis

del alphabet[0]  #error
alphabet.append("A") #error
alphabet.insert(0, "A") #error
"""

""" A única coisa que você pode fazer com del
em uma string, é remover a string como um todo"""



"""Isso pode """
alphabet = alphabet + "z"
alphabet = "a" + alphabet


#min() -list or String
print(min("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

"""Tabela ASCII – quais letras ocupam os
 primeiros locais – superior ou inferior?"""

#max() -list or String
print(max("aAbByYzZ"))


### index() method - retorna primeiro elemento
print("aAbByYzZaA".index("b"))

### list() function
print(list("abcabc"))

### count() method
print("abcabc".count("b"))

"""
https://docs.python.org/3.4/library/stdtypes.html#string-methods
"""

