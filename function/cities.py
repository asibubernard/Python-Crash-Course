"""Cities and their countries"""

def city_country(city, country):
    """Takes a city and its country and return a string"""
    city = "'" + city + ", " + country + "'" 
    return city.title()


ghanaian = city_country('accra', 'ghana')
british = city_country('london', 'britain')
german = city_country('berlin', 'germany')
print(ghanaian)
print(british)
print(german)
