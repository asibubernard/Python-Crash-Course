""" Positional Arguments """
def describe_pet(pet_name, animal_type='dog'):
    """ Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# Calling multiple functions
describe_pet('dog', 'yosty')
describe_pet('goat', 'gustav')
describe_pet('hen', 'akoko')

# Ordering mistakes with positional arguments
describe_pet('yosty', 'dog')

# Fixing the problem with Keyword Arguments
describe_pet(pet_name='yosty', animal_type='dog')
describe_pet(animal_type='dog', pet_name='yosty')

# Default value
describe_pet(pet_name='togo')

# Equilavent Function calls
# A dog named youknow.
describe_pet('youknow')
describe_pet(pet_name='youknow')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding Argument Error 
describe_pet()

