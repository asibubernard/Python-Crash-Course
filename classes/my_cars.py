from electric_car import *
from car import Car


my_beetle = Car('volkswagen', 'beetle', 2034)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2031)
print(my_tesla.get_descriptive_name())
