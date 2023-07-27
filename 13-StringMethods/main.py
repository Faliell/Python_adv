""" -A string original da qual o método é invocado
 não é alterada de forma alguma – a imutabilidade de uma string
  deve ser obedecida sem reservas;
    -A string modificada (neste caso, em letras maiúsculas) é retornada
 como resultado – se você não a usar de forma alguma
  (atribuí-la a uma variável ou passá-la para uma função/método)
  ela desaparecerá sem deixar vestígios."""

### capitalize()
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

###center():
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
#uso do caractere do segundo argumento, em vez de um espaço
print('[' + 'gamma'.center(20, '*') + ']')

### endswith()
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

### find()
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
#O segundo argumento especifica o índice no qual a pesquisa será iniciada
print('kappa'.find('a', 2))
"""não use find() se você quiser apenas verificar se um único caractere 
ocorre em uma string - o operador in será significativamente mais rápido."""



the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)


"""o terceiro argumento aponta para o primeiro índice que não
 será levado em consideração durante a pesquisa
  (na verdade é o limite superior da pesquisa)."""

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

### isalnum()
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

### isapha()
print("Moooo".isalpha())
print('Mu40'.isalpha())


### isdigit()
print('2018'.isdigit())
print("Year2019".isdigit())


### islower()
print("Moooo".islower())
print('moooo'.islower())


### isspace()
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())


### isupper()
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


### join()
print(",".join(["omicron", "pi", "rho"]))


### lower()
print("SiGmA=60".lower())


### lstrip()
print(" tau aa ".lstrip())
# remove os caracteres especificados do começo da string
print("www.python.com".lstrip("w."))
# se não achou, já para
print("pythoninstitute.org".lstrip(".org"))


### replace()
print("www.netacad.com".replace("netacad.com", "python.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
# O terceiro argumento (um número), limita o número de substituições.
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))





