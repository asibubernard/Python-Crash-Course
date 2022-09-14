""" Ask for a user's name and phone number"""

# the prompt for the user's name
# name = input("Please enter your name: ")
# # Reply with the answer from the prompt
# print("Hello, " + name + "!")
#
# name_2 = input("please enter your phone number: ")
# print(name + ", " + name_2 + " is your phone number")

prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nwhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
