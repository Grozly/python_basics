# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = str(input('Введите целое положительное число: '))

summ = (int(num) + int(num + num) + int(num + num + num))

print(f'Сумма числе (n + nn + nnn): {summ}')
