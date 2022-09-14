# Alien Colors -1 
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# Write an if statement to test whether the alien's color is green. if it is, print a message that the player just earned 5 point.

alien_color = 'red'
if alien_color == 'green':
    print("You've earned 5 points")
else: 
    print("You've lost your point")

# Alien colors -2
if alien_color == 'green':
    print("You've earned 5 points for shooting the alien")
elif alien_color == 'blue':
    print("You've earned 20 points for shooting the alien")
elif alien_color == 'yellow':
    print("You've earned nothing")
else: 
    print("You've earned 10")

# Stages of life - Using if-elif-else chain to determine
age = 7

if age < 2:
    print("My paddy you are baby oh")
elif age >=2:
    print("Man you are a toddler")
elif age >= 4:
    print("Man you are a kid")
elif age >= 13:
    print("You are a teenager")
elif age >= 20:
    print("Menua wo y3 big man")
elif age >= 65:
    print("Oluman")
else: 
    print("My paddy you do funeral oh")

# Favorite Fruit
favorite_fruits = ['orange', 'mango', 'banana', 'pear', 'strawberry']

if 'orange' in favorite_fruits:
    print("Asey you dey love Orange waa")
if 'mango' in favorite_fruits:
    print(favorite_fruits)
    print("I dey remove Mango from your list")
    favorite_fruits.remove('mango')
    print(favorite_fruits)
if 'banana' in favorite_fruits:
    print('banana'.title())


