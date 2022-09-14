# Testing tuples data structures
phone_numbers = ('0540795289', '0340795286', '0340795')
# phone_numbers[1] = '1234567890'  # assignment is not allowed in tuples
# phone_numbers.append('123456789')  # append function isn't allowed in tuples.
# print(phone_numbers)

# Print phone numbers in the phone_numbers tables.
for phone_number in phone_numbers:
    print(phone_number + ' was my first contact line.')

# Writing over a tuple
dimensions = (200, 50)
print('Original dimensions')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 300)
print('\nModified dimensions:')
for dimensions in dimensions:
    print(dimensions)

