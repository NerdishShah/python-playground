class Country:
    def __init__(self, name = 'Default'):
        self.name = name
    def instance_method(self):
        print('Instance menthod')


defaultCountry = Country()
india = Country('India')
india.instance_method();
print(defaultCountry.name)
print(india.name)
