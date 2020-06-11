# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class MassCount(Road):
    def __init__(self, _length, _width, volume1, volume2):
        super().__init__(_length, _width)
        self.volume1 = volume1
        self.volume2 = volume2

    def mass(self):
        return self._length * self._width * self.volume1 * self.volume2 / 10


countmass = MassCount(20, 5000, 25, 0.05)
print(f'Требуется - {countmass.mass()} тонн массы асфальта\nДля полотна {countmass._length}x{countmass._width} метров')
