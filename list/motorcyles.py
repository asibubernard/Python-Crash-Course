# Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki', 'royal']
print("List of Motorcycles")
print(motorcycles)

# changing an element - Update
print('\nChanging an element.')
motorcycles[0] = 'ducati'
print(motorcycles)

# ADDING
# Adding an element - using append function/method - Adds a new item
motorcycles.append('deguaa')
motorcycles.append('ebus')

print("\nAdded another bike brand...")
print(motorcycles)

# Insert an element
print("\nInserting an element at the begining of the list")
motorcycles.insert(0, 'ducati')
print(motorcycles)


# Removing an element - using append function/method  - Deletes an item from the list
# using del statment to delete the element
del motorcycles[-1]

# Using pop() method to remove an element from a list
print("""\nUsing pop() method to remove an element...\n
Pop() method singles out the last element...""")

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


# Popping item from any Position in a list
print("Popping item from any Position in a list...")
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


# Removing an item by value
print("\nRemoving an item by it value")
motorcycles.remove('ducati')

print(motorcycles)
