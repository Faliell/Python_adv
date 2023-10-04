"""Criando objetos de data e hora"""


"""
datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)
"""

import datetime

dt = datetime.datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())


# Criando uma data específica
data_especifica = datetime.datetime(2023, 8, 26, 15, 30, 0)
print("Data e hora específicas:", data_especifica)

# Obtendo apenas a data atual
data = data_especifica.date()
print("Data data_especifica:", data)

# Obtendo apenas o horário atual
hora = data_especifica.time()
print("Horário data_especifica:", hora)

"""
today() — retorna a data e hora local atual com o atributo tzinfo
definido como none, não aceita argumento

now() — retorna a data e hora local atual igual ao método today,
a menos que passemos o argumento opcional tz para ele. O argumento deste
método deve ser um objeto da subclasse tzinfo;

utcnow() — retorna a data e hora UTC atuais com o atributo tzinfo
definido como none.
"""

print("today:", datetime.datetime.today())
print("now:", datetime.datetime.now())
print("utcnow:", datetime.datetime.utcnow())