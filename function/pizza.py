"""
    Passing an Arbitrary number of Arguments.
    Mixing Positional and Arbitrary Arguments.
    """


def make_pizza(size, *toppings):
    """Summarize the Pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the follwing toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza( 14, 'pepperoni')
make_pizza(11, 'mushroom', 'green peppers', 'extra cheese')

