class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr(self.name)


class Student(Person):
    def __init__(self, name, college_name):
        super().__init__(name)
        self.college_name = college_name

    def __repr__(self):
        return repr((super().__repr__(), self.college_name))


class Device:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr(self.name)


class SmartPhone(Device):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def __repr__(self):
        return repr((super().__repr__(), self.model))


person = Person('Abdul')
student = Student('Abdul', 'The new college')
print(person)
print(student)

device = Device('Handheld')
smartPhone = SmartPhone('Handheld', 'iPhone 14')
print(device)
print(smartPhone)