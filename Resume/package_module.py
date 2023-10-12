print("I like to be a module.")

print(__name__)

"""
quando você executa um arquivo diretamente, sua variável __name__ é definida
como __main__;
quando um arquivo é importado como um módulo, sua variável __name__ é definida
como o nome do arquivo (excluindo .py)
"""


""" Pode informar aos seus usuários que esta é a sua variável,
que eles podem lê-la, mas que não devem modificá-la em nenhuma circunstância.
Isso é feito precedendo o nome da variável com _(um sublinhado) ou 
__(dois sublinhados), mas  é apenas uma convenção . Os usuários do seu módulo
podem obedecê-lo ou não."""

__counter = 0

if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")