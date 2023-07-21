print("I like to be a module.")

print(__name__)

"""quando você executa um arquivo diretamente, sua variável __name__ é definida como __main__;
quando um arquivo é importado como um módulo, sua variável __name__ é definida como
 o nome do arquivo (excluindo .py)"""


__counter = 0

if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")