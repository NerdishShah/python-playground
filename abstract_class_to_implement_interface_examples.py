from abc import ABC, abstractmethod


class GaminConsole(ABC):

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass


class MarioGame(GaminConsole):
    def up(self):
        print('Jumps')

    def down(self):
        print('Goes into hole')

    def left(self): pass

    def right(self): print('Move forward')


# game = MarioGame()
# game.right()
# game.up()
# game.right()
# game.down()


class ChessGame(GaminConsole):
    def up(self):
        print('Move piece up')

    def down(self):
        print('Move piece down')

    def left(self):
        print('Move piece left')

    def right(self):
        print('Move piece right')


games = [ChessGame(), MarioGame()]

for game in games:
    game.left()
    game.up()
    game.right()
    game.down()

#Duck Typing Example


class Human:

    def __init__(self):
        print('Duck Typing Example')

    def walk(self):
        print('Human can walk')


class Animal:
    def walk(self):
        print('Animal can walk')


species = [Human(), Animal()]

for s in species:
    s.walk()

