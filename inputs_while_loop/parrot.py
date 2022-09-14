""" Letting the User choose when to quit """

prompt = "\nTell me something, I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# message = ""
# Using a tag: This acts as a signal
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
