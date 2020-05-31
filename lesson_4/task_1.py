# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, rate_per_hour, prize = argv


def salary(hours, rate_per_hour, prize):
    return (int(hours) * int(rate_per_hour)) + int(prize)


print('Имя скрипта: ', script_name)
print('Часы: ', hours)
print('Ставка: ', rate_per_hour)
print('Премия: ', prize)
print('Зарплата: ', salary(hours, rate_per_hour, prize))
