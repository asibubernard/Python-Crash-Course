import json


def get_new_number():
    """Prompt user for favorite number."""
    favorite_number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
    return favorite_number


def get_stored_number():
    """Get and return stored number from user."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_object:
            number = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return number


def show_favorite_number():
    """Print number to user."""
    number = get_stored_number()
    if number:
        print("Yo you gave this number " + number)
    else:
        number = get_new_number()


show_favorite_number()

