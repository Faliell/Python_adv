""" Calendar Module"""


""" 
Day of the week	Integer     value	    Constant
Monday	                    0	        calendar.MONDAY
Tuesday	                    1	        calendar.TUESDAY
Wednesday	                2	        calendar.WEDNESDAY
Thursday	                3	        calendar.THURSDAY
Friday	                    4	        calendar.FRIDAY
Saturday	                5	        calendar.SATURDAY
Sunday	                    6	        calendar.SUNDAY
"""


import calendar
print(calendar.calendar(2023))


""" 
Parametros opcionais para formatação:
w – date column width (default 2)
l – number of lines per week (default 1)
c – number of spaces between month columns (default 6)
m – number of columns (default 3)
"""


""" prcal() """
import calendar
calendar.prcal(2023)


""" month()  prmonth()"""
import calendar
print(calendar.month(2023, 11))


""" setfirstweekday() """

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2023, 12)

""" weekday() """

import calendar
print(calendar.weekday(2023, 8, 28))


""" weekheader()
 
Exige que você especifique a largura em caracteres para um dia da semana. 
Se a largura fornecida for maior que 3, você ainda receberá os nomes
abreviados dos dias da semana com três caracteres."""

import calendar
print(calendar.weekheader(1))


""" isleap() leapdays()"""

import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.




