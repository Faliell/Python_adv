""" Creating time objects """


""" time(hour, minute, second, microsecond, tzinfo, fold) """

""" 
microsecond	must be greater than or equal to 0 and less than 1000000.
tzinfo	    The tzinfo parameter must be a tzinfo subclass object or None (default).
fold	    The fold parameter must be 0 or 1 (default 0).
"""

from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


""" The time module """


import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(2)


""" ctime()
 
converte o tempo em segundos desde 1º de janeiro de 1970 (época Unix)
em uma string.
"""

import time

timestamp = 1572879180
print(time.ctime(timestamp))

# sem argumento, data, hora atual
print(time.ctime())


""" gmtime() e localtime()
 
conhecimento da classe struct_time:

time.struct_time:
    tm_year   # Specifies the year.
    tm_mon    # Specifies the month (value from 1 to 12)
    tm_mday   # Specifies the day of the month (value from 1 to 31)
    tm_hour   # Specifies the hour (value from 0 to 23)
    tm_min    # Specifies the minute (value from 0 to 59)
    tm_sec    # Specifies the second (value from 0 to 61 )
    tm_wday    # Specifies the weekday (value from 0 to 6)
    tm_yday   # Specifies the year day (value from 1 to 366)
    tm_isdst  # Specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
    tm_zone   # Specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # Specifies the offset east of UTC (value in seconds)
"""

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))


""" A diferença entre eles é que a função gmtime retorna o objeto struct_time
em UTC, enquanto a função localtime retorna a hora local. Para a função gmtime,
o atributo tm_isdst é sempre 0."""


""" asctime() e mktime() """


timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))


""" 
asctime, converte um objeto struct_time ou uma tupla em uma string.
Observe que a familiar função gmtime é usada para obter o objeto struct_time.
Se você não fornecer um argumento para a função asctime, o tempo retornado
pela função localtime será usado.

mktime, converte um objeto struct_time ou uma tupla que expressa a
hora local no número de segundos desde a época do Unix. Em nosso exemplo,
passamos uma tupla para ele, que consiste nos seguintes valores

2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst
"""