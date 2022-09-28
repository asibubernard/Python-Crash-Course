from electric_car import Car, ElectricCar


my_tesla = ElectricCar('tesla', 'model Z', 2018)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


