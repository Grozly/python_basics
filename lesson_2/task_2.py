#  Для списка реализовать обмен значений соседних элементов, т.е.
#  Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#  При нечетном количестве элементов последний сохранить на своем месте.
#  Для заполнения списка элементов необходимо использовать функцию input().

my_list = [str(total_list) for total_list in input('Введите несколько элементов списка\n'
                                                   '(запишите их через пробел или знак ","): ').split()]
for total_list in range(1, len(my_list), 2):
    my_list[total_list - 1], my_list[total_list] = my_list[total_list], my_list[total_list - 1]

print(' '.join([str(total_list) for total_list in f'{my_list}']))
