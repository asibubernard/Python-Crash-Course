from users import User


class Privileges():
    """A simple attempt to mimic privileges of an administrator."""

    def __init__(self):
        """Initializes privileges attribute."""
        self.privileges = ['can add post', 'can delete post', 'can ban user',
                           'can view users']

    def show_privileges(self):
        """Prints all privileges of user."""
        print('--- List of Privileges ---')
       
        for privilege in self.privileges:
            print(privilege.title())


class Administrator(User):
    """A simple attempt to mimic an administrator."""

    def __init__(self, first_name, last_name, age):
        """Initializes all attributes of object."""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


# admin = Administrator('John', 'Antwi', 57)

# print(admin.first_name + ' ' + admin.last_name + ' is our first administrator, age ' + str(admin.age) + ' .')
# admin.privileges.show_privileges()
