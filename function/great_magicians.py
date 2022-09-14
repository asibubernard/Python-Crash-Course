"""Great Magiciains"""


def make_great(magicians, new_magicians):
    """
    Add a phrase to each name of a magician.
    Move modified to new_magician model.
    """
    print("---Old Magicians---")
    while magicians:
        magician = magicians.pop()
        # Add 'The Great' to each name
        print(magician.title())
        new_name = magician + ' The Great'
        new_magicians.append(new_name)


def show_magicians(new_magicians):
    """Print the names of magicians"""
    print("\n--- List of New Magicians ---")

    for name in new_magicians:
        print(name.title())

magicians = ['ato', 'maame', 'ebo', 'archie']
new_magicians = []


make_great(magicians, new_magicians)
show_magicians(new_magicians)

