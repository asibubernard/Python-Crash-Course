# Squares
print('Normal for loop')
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# List comprehension
print('\nList comprehension')
squares = [value**2 for value in range(1, 11)]
print(squares)
