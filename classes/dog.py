"""Class"""


class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age, color):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.color = color

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 5, 'white')
your_dog = Dog('lucy', 8, 'black')

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old and " + my_dog.color + " in color.")
my_dog.roll_over()
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old and " + your_dog.color + " in color.")
your_dog.sit()
your_dog.roll_over()


