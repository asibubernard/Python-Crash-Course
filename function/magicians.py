"""Magicians"""

def show_magicians(magicians):
    """Print the names of magicians"""
    for magician in magicians:
        print("\nName of magician: " + magician.title())


magicians = ['ato', 'maame', 'ebo', 'archie']

magic = show_magicians(magicians)
print(magic)

