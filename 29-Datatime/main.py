""" Obtendo a data local atual e criando objetos de data """


from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


""" criar data - ano, mês, dia """

my_date = date(2019, 11, 4)
print(my_date)


"""Criando um objeto de data a partir de timestamp"""

"""
No Unix, o carimbo de data/hora expressa o número de segundos desde
1º de janeiro de 1970, 00:00:00 (UTC). Esta data é chamada de época Unix,
porque foi quando começou a contagem do tempo nos sistemas Unix.

O timestamp é na verdade, a diferença entre uma data específica (incluindo a hora)
e 1º de janeiro de 1970, 00:00:00 (UTC), expressa em segundos.
"""

"""
Para criar um objeto de data a partir de um timestamp,
devemos passar um timestamp Unix para fromtimestamp 

módulo time, que fornece funções relacionadas ao tempo. Uma delas
é uma função chamada time(), que retorna o número de segundos desde
1º de janeiro de 1970 até o momento atual na forma de um número flutuante.
"""

from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)


""" Criando um objeto de data usando o formato ISO """

""" 
Método fromisoformat usa uma data no formato AAAA-MM-DD, compatível
com o padrão ISO 8601
"""


from datetime import date

date_string = "2023-08-25"
parsed_date = date.fromisoformat(date_string)

print(parsed_date)


""" replace() """


from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

""" 
Os parâmetros ano, mês e dia são opcionais
 
O método replace retorna um objeto de data alterado, portanto você
deve se lembrar de atribuí-lo a alguma variável. 
"""


""" weekday()
retorna o dia da semana como um número inteiro,
onde 0 é segunda-feira e 6 é domingo 
"""

d = date(2019, 11, 4)
print(d.weekday())


""" isoweekday()
que também retorna o dia da semana como um número inteiro,
mas 1 é segunda-feira e 7 é domingo
O número inteiro retornado pelo método segue a especificação ISO 85601.
"""

d = date(2019, 11, 4)
print(d.isoweekday())







