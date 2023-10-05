""" Clases para criação de calendários"""

""" 
calendar.Calendar – fornece métodos para preparar dados de calendário para formatação;

calendar.TextCalendar – é usado para criar calendários de texto regulares;

calendar.HTMLCalendar – é usado para criar calendários HTML;

calendar.LocalTextCalendar – é uma subclasse da classe calendar.TextCalendar.
O construtor desta classe usa o parâmetro locale, que é usado para retornar
os nomes apropriados dos meses e dias da semana.

calendar.LocalHTMLCalendar – é uma subclasse da classe calendar.HTMLCalendar.
O construtor desta classe usa o parâmetro locale, que é usado para 
os nomes apropriados dos meses e dias da semana.
"""


""" Criando um objeto Calendário
 
Recebe um parâmetro opcional, firstweekday, por padrão igual a 0 (segunda-feira). 

iterweekdays - que retorna um iterador para números de dias da semana.
"""

import calendar

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

print()


""" itermonthdates()
 
Como resultado, todos os dias do mês e ano especificados são retornados,
bem como todos os dias anteriores ao início ou ao final do mês que são
necessários para obter uma semana completa.
Cada dia é representado por um objeto datetime.date
"""

import calendar

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")

print()


""" itermonthdays() """

import calendar

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

print()

""" 
itermonthdays2 – retorna dias na forma de tuplas consistindo de um dia
do número do mês e um número do dia da semana;

itermonthdays3 – retorna dias na forma de tuplas que consistem em números de ano,
mês e dia do mês. 

itermonthdays4 – retorna dias na forma de tuplas que consistem em números de ano,
mês, dia do mês e dia da semana. 
"""


""" monthdays2calendar()
 
retorna uma lista de listas, onde cada sublista representa uma semana no mês especificado.
Cada elemento da sublista é uma tupla contendo um número que representa o dia do mês e um
código que indica o dia da semana. 
"""

import calendar

c = calendar.Calendar()

for data in c.monthdays2calendar(2023, 8):
    print(data)














