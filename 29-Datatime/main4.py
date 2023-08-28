""" Obtendo timestamp """


""" calcular um timestamp com base em uma determinada data e hora"""

from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())


""" 
Formatação de data e hora 
strftime()
"""

from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))


""" https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes"""

from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))


""" 
strftime() time module
também pode receber (opcionalmente) uma tupla ou um objeto struct_time.
"""

import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))


""" 
strptime() 
cria um objeto datetime a partir de uma string que representa uma data e hora
"""

from datetime import datetime

print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


""" No módulo time, você pode encontrar uma função chamada strptime,
analisa uma string que representa um tempo para um objeto struct_time
"""

import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


""" Date and time operations """


from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

""" Subtração cria um objeto timedelta"""


"""
Criando objetos timedelta:
argumentos aceitos pelo construtor da classe, que são:
days, seconds, microseconds, milliseconds, minutes, hours, weeks"""

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)


"""o objeto timedelta armazena apenas dias, segundos e
microssegundos internamente.
Semanas são convertidas em dias, horas e minutos em segundos e
milissegundos em microssegundos
"""

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)


""" Com operações """


from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)



