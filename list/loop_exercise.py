# Exercise one - Counting to twenty
print('Counting to twenty using for loop.')
for value in range(1, 21):
    print(value)

# Exercise Two - One million
print('Printing One to a thousand using for loop')
for value in range(1, 1001):
    print(value)

# Exercise Three - Summing a thousand
print('\nSumming a thousand using for loop')
digits = [value for value in range(1, 100, 2)]
print('\nThis a sum of thousand digits.')
print(sum(digits))


# Exercise four - Odd numbers
print('\n Using the argument of the range() function to make a list of',
      ('odd numbers.'))
for value in range(1, 101, 2):
    print(value)


# Exercise Five - Make a list of  multiples of 3 from 3 to 30.
print('\nMultiples of 3, 3 to 30.')
for value in range(1, 10):
    values = value * 3
    print(values)


multiples = [value*3 for value in range(1, 10)]
print(multiples)



values = []
for value in range(1, 10):
    values = value**3
    print(values)



print('Cubes - A number raised to the third power - eg 2**3...')
cubes = [value**3 for value in range(1,10)]
print(cubes)