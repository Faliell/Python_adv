"""Podem ser concatenados usando o operador +
e replicados usando o operador *"""

### Multiline
multiline = """Line #1
Line #2"""
#/n invisivel  - The escape character (\) is not counted
print(len(multiline))

### conhecer o valor do ponto de código ASCII/UNICODE de um caractere específico
print(ord("a"))

### obter o caractere correspondente
print(chr(33))

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

### NÃO aceita
### Python strings são imutáveis
""" A única coisa que você pode fazer com del
em uma string, é remover a string como um todo"""

#del alphabet[0]  #error
#alphabet.append("A")
#alphabet.insert(0, "A")

# Isso pode
alphabet = alphabet + "z"
alphabet = "a" + alphabet

#min() -list or String
print(min("aAbByYzZ"))

"""Tabela ASCII – quais letras ocupam os
 primeiros locais – superior ou inferior?"""

#max() -list or String
print(max("aAbByYzZ"))


### index() method
print("aAbByYzZaA".index("b"))

### list() function
print(list("abcabc"))

### count() method
print("abcabc".count("b"))

# https://docs.python.org/3.4/library/stdtypes.html#string-methods
