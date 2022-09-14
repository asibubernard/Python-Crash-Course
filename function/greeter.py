from formatted_name import get_formatted_name


#""" Example of a function """

# def greet_user(username):
#    """ Pass and  Display a simple greeting/info. """
#    print("Hello! " + username.title() + "!")

# This is an infinte loop!

while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")

    if f_name == 'q':
        break

    l_name = input("Last name: ")
    
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

