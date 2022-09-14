class Restaurant():
    """A simple restaurant model."""

    def __init__(self, name, cuisine, location, star):
        """Initialize name, cuisine and location attributes."""
        self.name = name
        self.cuisine = cuisine
        self.location = location
        self.star = star

    def describe_restaurant(self):
        """Description of a restaurant."""
        print(self.name.title() + " is the name a " + str(self.star) + " star restaurant.")
        print("It is located in " + self.location.title() + ".")
        print(self.cuisine.title() + " cuisine is used.")

    def open(self):
        """Simulate the time a restaurant opens."""
        print(self.name.title() + " is always open.")


restaurant_1 = Restaurant('greenland', 'chineese', 'swedru', 4)
restaurant_2 = Restaurant('golden tulip', 'spanish', 'accra', 5)
restaurant_3 = Restaurant('movempick', 'african', 'accra', 5)


print(restaurant_1.name.title() + " is my favorite restaurant.")
restaurant_1.describe_restaurant()
restaurant_1.open()

print("\n " + restaurant_2.name.title() + ' is one of my favorite.')
restaurant_2.describe_restaurant()
restaurant_2.open()

print("\n " + restaurant_3.name.title() + ' is another one of my favorite restaurants.')
restaurant_3.describe_restaurant()
restaurant_3.open()




