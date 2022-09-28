from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """A simple model of a restaurant."""
    def __init__(self, name, cuisine, location, star):
        super().__init__(name, cuisine, location, star)
        self.flavors = ['chocolate', 'strawberyy', 'vanilla']

    def display_flavors(self):
        """Print flavors of Ice cream."""
        print('--- List of Flavors ---')

        for flavor in self.flavors:
            print(flavor)


ice_cream = IceCreamStand('MyPaddyRestaurant', 'Italiano', 'Berlin', 4)
print(ice_cream.name + ' is my favorite Ice Cream Joint.')
print(ice_cream.cuisine + ' is their cuisine.')
print(str(ice_cream.star) + ' restaurant.')
ice_cream.display_flavors()

