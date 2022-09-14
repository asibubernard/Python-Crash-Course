"""Sandwiches"""


def make_sandwich(*toppings):
    """Make a sandwich with various toppings"""
    print("\nThe following are toppings you ordered for your sandwich.")
    for topping in toppings:
        print('- ' + topping.title())


make_sandwich('moko', 'onion', 'sugar')
make_sandwich('efo', 'ghana', 'atis', 'camidoh')
