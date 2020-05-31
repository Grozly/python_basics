#  Пользователь вводит месяц в виде целого числа от 1 до 12.
#  Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#  Напишите решения через list и через dict.

# Использование списка list
seasons = ['Зима', 'Весна', 'Лето', 'Осень']

month_num = int(input('Введите номер месяца (от 1 до 12): '))

if 12 >= month_num >= 1:
    if month_num == 1 or month_num == 2 or month_num == 12:
        print(f'{month_num}-й месяц, время  года {seasons[0]}')
    elif month_num == 3 or month_num == 4 or month_num == 5:
        print(f'{month_num}-й месяц, время года {seasons[1]}')
    elif month_num == 6 or month_num == 7 or month_num == 8:
        print(f'{month_num}-й месяц, время года {seasons[2]}')
    else:
        print(f'{month_num}-й месяц, время года {seasons[3]}')
else:
    print(f'Вы ввели неверные данные, введите номер месяца от 1 до 12')

# Использование словаря dict
month_num = int(input('Введите номер месяца (от 1 до 12): '))

if 12 >= month_num >= 1:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентябрь',
                  10: 'Октябрь',
                  11: 'Ноябрь',
                  12: 'Декабрь'}
    season_dict = {1: 'Зима',
                   2: 'Весна',
                   3: 'Лето',
                   4: 'Осень'}
    if 2 >= month_num >= 1 or month_num == 12:
        print(f'{month_dict[month_num]} - Это {month_num}-й месяц времени года {season_dict[1]}')
    elif 3 <= month_num <= 5:
        print(f'{month_dict[month_num]} - Это {month_num}-й месяц времени года {season_dict[2]}')
    elif 6 <= month_num <= 8:
        print(f'{month_dict[month_num]} - Это {month_num}-й месяц времени года {season_dict[3]}')
    elif 9 <= month_num <= 11:
        print(f'{month_dict[month_num]} - Это {month_num}-й месяц времени года {season_dict[4]}')
else:
    print(f'Вы ввели неверные данные, введите номер месяца от 1 до 12')
