class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, _model, _color, _engine_power):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color

    def get_model(self):
        print(f'Модель: {self._model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self._engine_power}')

    def get_color(self):
        print(f'Цвет: {self._color}')

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Имя владельца: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f'Нельзя сменить на {new_color}')


class Sedan(Vehicle):
    _PASSENGER_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
