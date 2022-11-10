import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Test for 'city_functions.py'"""

    def test_city_and_country(self):
        """Does 'Berlin, Germany' works?"""
        city = city_country('berlin', 'germany')
        self.assertEqual(city, 'Berlin, Germany')
        
    def test_city_country_population(self):
        """Does 'Wien, Austria, Population 32000' work?"""
        city = city_country('wien', 'austria', '32000')
        self.assertEqual(city, 'Wien, Austria - Population 32000')


unittest.main()
