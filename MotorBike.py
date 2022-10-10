class MotorBike:

    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def __repr__(self):
        return repr((self.gear, self.speed))


honda = MotorBike(1, 50)

yamaha = MotorBike(2, 120)

print(honda)
print(yamaha)
