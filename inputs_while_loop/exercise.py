""" Deli - Using while Loop to modify a List """
# Start with list of various sandwich orders and empty lits of 
# finished sandwiches.
sandwich_orders = ['sand_w_1', 'sand_w_2', 'sand_2_3', 'sand_w@', 'sand_w@', 'sand_w@']
finished_sandwiches = []

# Confirm each the various sandwich orders.
# Move each confirmed sandwich into the list of finished sandwiches.
print(sandwich_orders)

print("\nDeli has run out of sand_w@")

# Removing all 'sand_w@' items from sandwich orders.
while 'sand_w@' in sandwich_orders:
    sandwich_orders.remove('sand_w@')

print(sandwich_orders)


# Whiles sandwich orders list isn't empty
while sandwich_orders:
    # Remove the last order in the list 
    new_sandwich_order = sandwich_orders.pop()

    print("\nI made your " + new_sandwich_order + ".")
    finished_sandwiches.append(new_sandwich_order)

# Display all finished sandwich orders.
print("\nThe following sandwiches have been finished.")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())


""" Dream Vacation - Accepting User generated data. """
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which city would you love to go during vacation? ")

    # Store the response in the dictionary 
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("would you like to let another person respond? (yes/ no) ")

    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results
print("\n--- Polling Results ---")
for name, response in responses.items():
       print(name + " would love to have vacation in " + response)


