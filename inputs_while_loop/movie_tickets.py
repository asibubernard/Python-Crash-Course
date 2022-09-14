""" Movie Tickets: charging different tickets depending on age. """

age = input("Please what your age?\n(Enter 'quit' to end thd program.) ")
age = int(age)

active = True
while active:

    # if str(age) == 'quit':
    #     break
    if age <= 3:
        print("Your admission is free...")
        break
    elif age > 4:
        print("Please children above 3 are to pay $10.")
        break

