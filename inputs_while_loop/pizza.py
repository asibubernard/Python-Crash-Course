""" Pizza Toppings """
# Loop to ask for pizza toppings

prompt = "\nPlease tell me the series of pizza toppings you need..."
prompt += "\n(Enter 'quit' to end it.) "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message + " will be added to your pizza. ")
