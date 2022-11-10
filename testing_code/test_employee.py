import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """Create an employee and give salary to enable testing."""
        self.employee = Employee('Ato', 'Asibu')
      
    def test_give_default_raise(self):
        """Test to find the default salary of an employee is 5000."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 5000)

    def test_give_custom_raise(self):
        """Test to find out custom salary of an employee."""
        self.employee.give_raise(4000)
        self.assertEqual(self.employee.annual_salary, 4000)
    
    def test_for_data_being_stored(self):
        """Test for the storage of data."""
        self.assertIn(self.employee.last_name, 'Asibu')


unittest.main()
