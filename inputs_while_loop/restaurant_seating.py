""" Ask user how many people are in their dinner group if answer is more than eight print a message they'd have to wait
otherwise the table is read. """

dinner_group = input("Hello there, how many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group <= 8:
    print("Please your dinner table is ready...")
else:
    print("Please you guys would have to wait!...")
