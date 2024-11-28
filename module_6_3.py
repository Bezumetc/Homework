from random import randint

class Animal:

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed

        if new_z < 0:
            print(f'Its too deep, i can dive')
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f'Sorry, i`m peaceful :)')
        else:
            print(f'Be careful, i`m attacking you O_O')

class Bird(Animal):

    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {randint(1,4)} eggs for you')

class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        new_z = self._cords[2] - abs(dz) * 0.5 * self.speed
        self._cords[2] = max(new_z, 0)

class PoisonousAnimal(Animal):

    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):

    sound = 'Click-click-click'

    def __init__(self, speed):
        super().__init__(speed)

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()