#  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#  speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
#  которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула влево'

    def turn_right(self):
        return f'{self.name} повернула вправо'

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed} км/ч'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'TownCar {self.name} едет со скоростью {self.speed} км/ч')

        if self.speed > 60:
            return f'TownCar {self.name} привышает скорость'
        return f'TownCar {self.name} соблюдает скоростной режим'

    def police(self):
        if self.is_police:
            return f'{self.name} является полецейской машиной'
        return f'{self.name} не является полецейской машиной'


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} является полецейской машиной'
        return f'{self.name} не является полецейской машиной'


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'WorkCar {self.name} едет со скоростью {self.speed} км/ч')

        if self.speed > 60:
            return f'WorkCar {self.name} привышает скорость {self.speed} км/ч'
        return f'WorkCar {self.name} соблюдает скоростной режим {self.speed} км/ч'

    def police(self):
        if self.is_police:
            return f'{self.name} является полецейской машиной'
        return f'{self.name} не является полецейской машиной'


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} является полецейской машиной'
        return f'{self.name} не является полецейской машиной'


hunday = TownCar(80, 'Белый', 'Hunday', False)
bmw = SportCar(220, 'Черный', 'BMW', False)
suzuki = WorkCar(25, 'Желтый', 'Suzuki', False)
lexus = PoliceCar(98, 'Синий', 'Lexus', True)

print(f'{hunday.turn_right()}\n'
      f'{hunday.go()}\n'
      f'{hunday.show_speed()}\n'
      f'За привышение скорости машину остановили\n'
      f'{hunday.stop()}')

print(f'{lexus.police()}\n'
      f'Полиция выписала штраф и\n'
      f'{lexus.go()}\n'
      f'{lexus.show_speed()}\n'
      f'За следующим преступником')

print(f'{bmw.go()} от полицейской машины\n'
      f'{bmw.show_speed()}\n'
      f'{bmw.police()}\n'
      f'{bmw.turn_left()} и быстро оторвалась от погони')

print(f'{suzuki.go()}\n'
      f'{suzuki.show_speed()} и не нарушает закон')
