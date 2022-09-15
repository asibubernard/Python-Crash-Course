class Restaurant():
    """A simple restaurant model."""

    def __init__(self, name, cuisine, location, star,):
        """Initialize name, cuisine and location attributes."""
        self.name = name
        self.cuisine = cuisine
        self.location = location
        self.star = star
        self.number_served = 0

    def describe_restaurant(self):
        """Description of a restaurant."""
        print(self.name.title() + " is the name a " + str(self.star) + " star restaurant.")
        print("It is located in " + self.location.title() + ".")
        print(self.cuisine.title() + " cuisine is used.")
        print(self.name.title() + " has served " + str(self.number_served) + ' customers.')
        
    def open(self):
        """Simulate the time a restaurant opens."""
        print(self.name.title() + " is always open.")

    def set_number_served(self, number):
        """Sets the number of customers that have been served."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't have a negative number.")
      
    def increment_number_served(self, number):
        """Increase the number of customers served."""
        self.number_served += number
    

restaurant_1 = Restaurant('greenland', 'chineese', 'swedru', 4)
restaurant_2 = Restaurant('golden tulip', 'spanish', 'accra', 5)
restaurant_3 = Restaurant('movempick', 'african', 'accra', 5)


print(restaurant_1.name.title() + " is my favorite restaurant.")
restaurant_1.set_number_served(34)
restaurant_1.describe_restaurant()
restaurant_1.open()

print("\n" + restaurant_2.name.title() + ' is one of my favorite.')
restaurant_2.set_number_served(869)
restaurant_2.increment_number_served(100)
restaurant_2.describe_restaurant()
restaurant_2.open()

print("\n" + restaurant_3.name.title() + ' is another one of my favorite restaurants.')
restaurant_3.set_number_served(57)
restaurant_3.increment_number_served(9)
restaurant_3.describe_restaurant()
restaurant_3.open()




