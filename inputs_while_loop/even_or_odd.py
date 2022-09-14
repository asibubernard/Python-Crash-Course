""" Even or Odd numbers """

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

# modulo means remainder after division.
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
