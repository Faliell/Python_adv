""" Exeções Úteis """
"""
ArithmeticError

Location: BaseException ← Exception ← ArithmeticError
Descrição: uma exceção abstrata incluindo todas as exceções causadas por operações
aritméticas como divisão zero ou domínio inválido de um argumento


AssertionError

Location: BaseException ← Exception ← AssertionError
Descrição: uma exceção concreta gerada pela instrução assert quando seu argumento
é avaliado como False, None, 0ou uma string vazia


BaseException

Location: BaseException
Descrição: a mais geral (abstrata) de todas as exceções do Python - todas as outras
exceções estão incluídas nesta; pode-se dizer que os dois seguintes, exceto ramos,
são equivalentes: "except:" e "except BaseException:".


IndexError

Location: BaseException ← Exception ← LookupError ← IndexError
Descrição: uma exceção concreta gerada quando você tenta acessar um elemento de uma 
sequência inexistente (por exemplo, um elemento de uma lista)


KeyboardInterrupt

Location: BaseException ← KeyboardInterrupt
Descrição: uma exceção concreta levantada quando o usuário utiliza um atalho de 
teclado projetado para encerrar a execução de um programa ( Ctrl-C na maioria dos
sistemas operacionais); se o tratamento desta exceção não levar ao encerramento do
programa, o programa continuará sua execução.
Nota: esta exceção não é derivada da classe Exception .


LookupError

Location: BaseException ← Exception ← LookupError
Descrição: uma exceção abstrata incluindo todas as exceções causadas por erros
resultantes de referências inválidas a diferentes coleções (listas, dicionários,
tuplas, etc.)


MemoryError

Location: BaseException ← Exception ← MemoryError
Descrição: uma exceção concreta gerada quando uma operação não pode ser concluída
devido à falta de memória livre.


OverflowError

Location: BaseException ← Exception ← ArithmeticError ← OverflowError
Descrição: uma exceção concreta gerada quando uma operação produz um número grande
demais para ser armazenado com êxito


ImportError

Location: BaseException ← Exception ← StandardError ← ImportError
Descrição: uma exceção concreta gerada quando uma operação de importação falha


KeyError

Location: BaseException ← Exception ← LookupError ← KeyError
Descrição: uma exceção concreta gerada quando você tenta acessar um elemento
inexistente de uma coleção (por exemplo, um elemento de dicionário)
"""


"""
1. Algumas exceções abstratas integradas ao Python são:

ArithmeticError,
BaseException,
LookupError.

2. Algumas exceções concretas integradas ao Python são:

AssertionError,
ImportError,
IndexError,
KeyboardInterrupt,
KeyError,
MemoryError,
OverflowError.
"""
