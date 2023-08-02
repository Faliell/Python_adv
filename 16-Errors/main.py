"""Quando Python acha um erro:
-ele interrompe o seu programa;
-ele cria um tipo especial de dados, chamado exceção."""

# Momento que chama except
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")

#####################################
# # Qual o erro?
#
# # exemplo 1:
#
# try:
#     print("Let's try to do this")
#     print("#"[2])
#     print("We succeeded!")
# except:
#     print("We failed")
# print("We're done")
#
# # exemplo 2:
#
# try:
#     print("alpha"[1/0])
# except ZeroDivisionError:
#     print("zero")
# except IndexError:
#     print("index")
# except:
#     print("some")
###########################################

