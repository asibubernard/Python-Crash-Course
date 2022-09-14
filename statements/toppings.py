available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms.")
#if 'extra cheese' in requested_toppings:
#    print("Adding extra cheese")
#if 'dawadawa' in requested_toppings:
#    print("No other toppings")
 
# checking for special item
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("\nMy paddy I'm sorry we no get green peppers right now.")
#    else:
#        print("\nAdding " + requested_topping + ".")

#print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nfinished making your pizza!")
