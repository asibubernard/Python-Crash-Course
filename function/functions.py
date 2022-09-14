import pizza
from profile import build_profile
from magicians import show_magicians as sm
import cars as c
from cities import *

# pizza
pizza.make_pizza(12, 'kaffee')
pizza.make_pizza(31, 'kellner', 'wurst', 'extra kase')

# profile
user_profile = build_profile('Ebo', 'Asibu', 29, location='Berlin',
                             field='Programming', net_worth='$1 Billion')
print(user_profile)

# magicians
magicians = ['wo', 'ist', 'wien', 'deutchland', 'amerika']
magic = sm(magicians)
print(magic)

# cars
toyota = c.make_car('Toyota', 'C499', color='Yellow', transmission='Manual', tow_package=True)
print(toyota)

# cities
german = city_country('berlin', 'germany')
print(german)


# cars

