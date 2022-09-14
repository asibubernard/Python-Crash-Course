""" Removing all instances of specifc values from a list """

pets = ['dog', 'mosquito', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'mosquito' in pets:
    pets.remove('mosquito')

print(pets)

