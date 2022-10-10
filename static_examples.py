class Employee:
    headcount = 0

    def __init__(self, name):
        self.name = name
        Employee.headcount += 1

    @staticmethod
    def get_headcount():
        return Employee.headcount


emp1 = Employee('Shahul')
emp2 = Employee('Abdul')


#Never assign value using instance variable but using class
# emp1.headcount = 100
# Employee.headcount = 100

print(Employee.headcount)
print(emp1.headcount)
print(Employee.get_headcount())
