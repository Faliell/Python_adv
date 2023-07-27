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