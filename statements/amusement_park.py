# Testing if-elif-else statements
# Pseudo code
# Admission for anyone under 4 is free.
# Admission for anyone between the ages of 4 and 18 is $15.
# Admission for anyone age 18 or older is $10.
# Admission for anyone age 65 or older is $5.

age = 12 

if age < 4:
    print("Your admission cost $0.")
elif age < 18:
    print("Your admission cost $15.")
else: 
    print("Your admission cost $10.")

# Multiple use of elif blocks

age =44

if age < 4:
    price = 0
elif age < 18:
    price = 15
elif age < 65: 
    price = 10
elif age >= 65:
    price = 5 

print("\nYour admission cost is $" + str(price) + ".")

# Omitting the else Block

