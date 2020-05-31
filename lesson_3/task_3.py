# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    """
    :param num1: Принимает первое целое число
    :param num2: Принимает второе целое число
    :param num3: Принимает третье целое число
    :return: summ_: Возвращает сумму двух наибольших чисел
    """
    total = [num1, num2, num3]
    result = []
    max1 = max(total)
    result.append(max1)
    total.remove(max1)
    max2 = max(total)
    result.append(max2)
    total.remove(max2)
    summ_ = sum(result)
    return summ_


print(my_func(20, -8, 1))
