def city_country(city, country, population=''):
    """Return a City and it's country."""
    if population:
        city_country = city + ', ' + country + ' - Population ' + population
    else:
        city_country = city + ', ' + country
    return city_country.title()

