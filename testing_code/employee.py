class Employee():
    """A simple model of an Employee"""

    def __init__(self, first_name, last_name):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = 0

    def give_raise(self, salary=""):
        """Give a raise of $5000 by default or custom amount."""
        if salary:
            self.annual_salary += salary
        else:
            self.annual_salary += 5000



