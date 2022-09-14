""" CREATE OPERATION """
""" Creating a dictionary in a list """
print("Creating a list of dictionary objects")
persons = []

# repeat in the range of 5
for person in range(1, 6):
    # assign an object/dictionary to person variable
    person = {'name': 'maame', 'age': 24}
    # add person to persons list
    persons.append(person)
    # print to show the created persons/objects
print(persons)

""" We can also use LIST COMPREHENSION """
# Create persons dictionary data using list comprehension 
print("\nUsing list comprehension to create dictionary objects")
persons = [{'name': 'ebo', 'age': 23} for person in range(1, 6)]
print(persons)


""" Putting a list in dictionary object """


""" READ OPERATION """
""" Reading items from a dictionary """
print("\nReading items from a dictionary")
person = {'first_name': 'bernard', 'last_name': 'asibu'}

# Repeat the following process for each item.
for value, key in person.items():
    # show the values in dictionary
    print("Value: " + value)
    # show the keys in dictionary 
    print("Key: " + key)

# viewing only values from a dictionary
print("Reading only values from a dictionary")
# for every each value in the dictionary
for value in person.values():
    # show the value in the dictionary
    print(value + "--- Values")

# viewing only keys from a dictionary 
print("\nReading only keys from a dictionary")
# for every key in person object
for key in person.keys():
    # show the key in the dictionary
    print(key + " is a key from person")


""" UPDATE OPERATION """
print("\nUsing the update operation in dictionary")
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(0, 10):
    new_alien = {'color': 'green', 'points': '6', 'speed': 'slow'}
    aliens.append(new_alien)

# from the 1st alien to the 3rd alien in aliens dictionary
for alien in aliens[0:3]:
    # check if the color of the alien is green and if true
    if alien['color'] == 'green':
        # change the color of the alien to yellow
        alien['color'] = 'yellow'
        # change the speed of the alien to medium
        alien['speed'] = 'medium'
        # change the points of the alien to 10
        alien['points'] = 10
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 9

# Show the first 5 aliens:
for alien in aliens[0:3]:
    print(alien)
print(...)

""" DELETE OPERATION """
