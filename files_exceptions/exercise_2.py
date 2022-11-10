# Guest 
# A simple program to write quest names from a response to a file.

# Ask for name of user
# name = input("Whats your name? ")

# file
# filename = 'guest.txt'

# Write name to file
# with open(filename, 'w') as file_object:
#    file_object.write(name)

# Guest Book
# While loop that prompts users for their name and stores it.

# filename = 'text_files/guest_book.txt'

# while True:
   # guest_book = input("Please what's your name? ")
   # print("You welcome " + guest_book)

   #  with open(filename, 'w') as file_object:
       # file_object.write(guest_book)

   # break

# Programming Poll
# Ask people why they like programming.
def programming_poll():
    filename = 'programming_poll.txt'

    while True:
        programming_poll = input("Why programming? ")

        with open(filename, 'a') as file_object:
            file_object.write(programming_poll())


print(programming_poll())
