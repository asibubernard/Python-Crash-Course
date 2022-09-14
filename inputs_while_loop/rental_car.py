''' Program that asks for the kind of rental car a user would like. '''

prompt = "What kind of rental car would you like to rent? "
# prompt += "\nBenz or Mercedez? "

rental_car = input(prompt)
if rental_car == 'Benz':
    print("Alright " + rental_car + " is available for $200 per day.")
elif rental_car == 'Mercedez':
    print("Sorry the " + rental_car + " isn't available.")
else:
    print("We don't have " + rental_car + ".")
