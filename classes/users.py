"""Users"""


class User():
    """A simple attempt to model profile of a user."""

    def __init__(self, first_name, last_name, age):
        """Initilizes first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Describe the user."""
        print(self.first_name.title() + " " + self.last_name.title() + " ist " + str(self.age) + " Jahre.")
        print(self.first_name.title() + ' hat ' + str(self.login_attempts) + ' mal versucht sich anzumelden.')

    def greet_user(self):
        """Greet the user."""
        full_name = self.first_name + " " + self.last_name
        print("\nHallo " + full_name.title() + " gerne geschehen.")
    
    def increment_login_attempts(self):
        """Increment the value of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to Zero 0."""
        self.login_attempts = 0

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.first_name!r}, {self.last_name!r}, {self.age!r})')
                

user = User('ebo', 'asibu', 29)
print("\n " + user.first_name.title() + " ist " + str(user.age) + " Jahre.")
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()
user.reset_login_attempts()
user.describe_user()


user_2 = User('ato', 'asibu', 18)
print("\n " + user_2.first_name.title() + " ist " + str(user_2.age) + " Jahre.")
user_2.greet_user()
user_2.describe_user()
