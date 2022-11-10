import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Ask user if the username is correct if not get new username."""
    username = get_stored_username()
    print("Answer the question with yes or no...")
    response_from_user = input("Is " + username.title() + " your username?  ")
    if response_from_user.lower() == 'yes':
        print('Welcome back ' + username.title())
    else:
        username = get_new_username()
        print(username.title() + " we'll remember you when you return.")


greet_user()

