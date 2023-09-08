""" A relação final entre strings é determinada comparando o primeiro
caractere diferente em ambas as strings (tenha sempre em mente os pontos
 de código ASCII/UNICODE)."""

print('alpha' == 'alpha')
print('alpha' != 'Alpha')


# idêntica ao início da mais longa, a string mais longa é considerada maior.
print('alpha' < 'alphabet')

# letras maiúsculas são consideradas menores que as minúsculas
print('beta' > 'Beta')

# se uma string contém apenas dígitos, ainda não é um número.
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')

# Comparar strings com números geralmente é uma má ideia.
# Únicas comparações  == e !=
print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
# print('10' > 10) # error


""" Ordenação sorted() sort()"""

# Sorted() - retorna nova lista, não altera original

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# sort() - altera original
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)


# conversão

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

"""  é possível somente quando a string representa um número válido."""
# reverso:
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)
# errado = int('1.3')
print(itg + flt)




