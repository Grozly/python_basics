# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class СlothesAll:
    def __init__(self, W, H):
        self.W = W
        self.H = H

    def get_square_coat(self):
        return self.W / 6.5 + 0.5

    def get_square_jacket(self):
        return self.H * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани\n'
                   f'{(self.W / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(СlothesAll):
    def __init__(self, W, H):
        super().__init__(W, H)
        self.square_c = round(self.W / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(СlothesAll):
    def __init__(self, W, H):
        super().__init__(W, H)
        self.square_j = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'


coat = Coat(1, 3)
jacket = Jacket(1, 4)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_coat())
print(jacket.get_square_jacket())