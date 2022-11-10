import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Maame Gyesiwah' work?"""
        formatted_name = get_formatted_name('maame', 'gyesiwah')
        self.assertEqual(formatted_name, 'Maame Gyesiwah')
    
    def test_first_last_middle_name(self):
        """Do names like 'Ato Aboagye nyarko' work?"""
        formatted_name = get_formatted_name('ato', 'aboagye', 'nyarko')
        self.assertEqual(formatted_name, 'Ato Nyarko Aboagye')


unittest.main()
