""" Try it yourself """

# T-Shirt
def make_shirt(size='large'):
    """ Accept and display size of T-shirt """
    if size == 'small':
        print("\nYour size is " + size + " hence we will print this in your shirt")
        print("The message below would be on your shirt")
        print("I LOVE JAVASCRIPT")
    elif size == 'medium':
        print("\nYour size is " + size + " hence we will print this in your shirt")
        print("The message below would be on your shirt")
        print("I LOVE JAVA")
    else:
        print("\nThe size of your T-shirt is " + size + ".")
        print("The message below would be on your shirt")
        print("I LOVE PYTHON")
    
make_shirt(size='small')
make_shirt('medium')
make_shirt()


# Cities
def describe_city(city, country='Iceland'):
    print("\n" + city + " is in " + country + ".")
    
describe_city('Accra')
describe_city('London', country='BRITAIN')
describe_city(city='Tamale', country='Ghana')
