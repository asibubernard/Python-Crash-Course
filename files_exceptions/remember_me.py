# Saving user generated data
import json
from json import JSONDecoder as js


# Load the username, if it has been stored previously.
# Else prompt for the username and store it.
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


def greet_user():
    """Greet the user by name."""
    try:
        username = get_stored_username()
        if username:
            print("Welcome " + username + ", thanks for coming!")
    except js:
        print("Please you don't have any username stored.")
        username = get_username()
        print("You are welcome " + username + "!")
    else:
        get_username()
    # else:
        # print("We couldn't find your name our system.")
          
        # username = input("What is your name? ")
        # filename = 'username.json'
        # with open(filename, 'w') as f_obj:
            #  json.dump(username, f_obj)
            #  print("We'll remember you when you come back, " + username + "!")


def get_username():
    username = input("What is your name? ")
    filename = 'username.json'
    try:
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    except FileNotFoundError:
        print(f"Sorry {filename} isn't available.")
    else:
        print("We'll remember you return " + username + "!")


greet_user()

