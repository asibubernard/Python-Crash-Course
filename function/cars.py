"""Cars"""


def make_car(manufacturer, model, **key_features):
    """Stores information about a car"""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model 
    
    for key, value in key_features.items():
        car[key] = value

    return car


mercedez = make_car('Mercedez', 'C300', color='Black', transmission='Automatic',
                    tow_package=True)
print(mercedez)
