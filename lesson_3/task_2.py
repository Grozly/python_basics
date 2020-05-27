# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_func(name, surname, birthday, city, email, phone):
    """
    :param name: Принимает имя
    :param surname: Принимает фамилию
    :param birthday: Принимает год рождения
    :param city: Принимает город
    :param email: Принимает email
    :param phone: Принимает телефон
    :return: Возвращает name, surname, birthday, city, email, phone
    """
    return f'Имя: {name}, Фамилия: {surname}, ' \
           f'Год рождения: {birthday}, ' \
           f'Город: {city}, Email: {email}, Телефон: {phone}'


print(user_func(name='Иван', surname='Иванов',
                birthday=1993, city='Москва',
                email='qwerty@mail.ru', phone=89025456789))

