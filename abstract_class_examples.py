from abc import ABC, abstractmethod


class AbstractRecipe(ABC):
    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.clean_up()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dish(self):
        pass

    @abstractmethod
    def clean_up(self):
        pass


class Recipe(AbstractRecipe):

    def get_ready(self):
        print('Get raw materials')
        print('Get utensils')

    def do_the_dish(self):
        print('Do the dish')

    def clean_up(self):
        print('Clean Utensils')


recipe = Recipe()
recipe.execute()

