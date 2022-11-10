""" Dictionary in dictionary """

cities = {'toronto': {'country': 'canada', 'population': '2million'},
          'new_york': {'country': 'usa', 'population': '20 million'},
          'berlin': {'country': 'germany', 'population': '500 thousand'}}

for city, city_info in cities.items():
    print(city.title(), " is city in ", city_info['country'], " with a population of ",  city_info['population'])
