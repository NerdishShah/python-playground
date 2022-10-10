class LandAnimals:
    def walk(self):
        print('Walk')


class WaterAnimals:
    def swim(self):
        print('Swim')


class Ambiphian(LandAnimals, WaterAnimals):
    pass


frog = Ambiphian()
frog.walk()
frog.swim()
