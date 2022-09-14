# Dictionary notes
# Create A dictionary of my family members
my_family = {"father": 'michael', 'mother': 'elizabeth', 'sister': 'sophia', 'brother_1': 'richard',
             'brother_2': 'moses'}

# View data from a dictionary - Loop
# for key, value in my_family.items():
#    print(value + " is my " + key)
# for position, name in my_family.items():
#    print("\n"+ name.title() + " is my " + position.upper())

# Add an item to dictionary items.
# my_family['brother_3'] = 'bernard'
# print(my_family)

# Modify or Update a dictionary
# print("\nI'm updating my sister's name in the dictionary... Below is the old dictionary.")
# print(my_family)
# my_family['sister'] = 'maame'
# print("Updated dictionary\n")
# print(my_family)

# Looping and updating a dictionary item
person = {'first_name': 'bernard', 'last_name': 'asibu', 'age': 28, 'occupation': 'software developer'}
# Printing values from a dictionary 
# for value in person.values():
#    print("This is a value from person " + str(value))

# Printing keys from a dictionary 
# for key in person.keys():
#    print("This is a key from person " + key)

# Loop and update values in dictionary
for key in person.items():
    if key == 'first_name':
        person['first_name'] = 'ebus'
    else:
        print("These are keys from Ebo Asibu " + key) 

