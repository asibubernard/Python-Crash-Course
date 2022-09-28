"""Using randint() to make a dice."""
from random import randint


class Dice():
    """A simple model to represent a dice."""

    def __init__(self):
        """Initializes attribute"""
        self.sides = 6

    def roll_die(self, number=''):
        """Prints a random number between 1 and number of size the die has."""
      
        if number:
            result = randint(1, number)
            print(result)
        else:
            result = randint(1, self.sides)
            print(result)


my_die = Dice()
my_die.roll_die(8)

