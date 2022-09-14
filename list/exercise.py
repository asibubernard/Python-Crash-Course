# List excersise
# Guest List
guest_list = ['ato', 'maame', 'archie']
message = "you are invited to my birthday party celebration."
print(guest_list)


# guests
first_guest = guest_list[0]
second_guest = guest_list[1]
third_guest = guest_list[2]

# Invitation to guests
print(first_guest.title() + ' ' + message)
print(second_guest.title() + ' ' + message)
print(third_guest.title() + ' ' + message)

# Changing Guest List
print(third_guest.title() + ' ' +
"""(can't make it to the party hence this is our new list.""")

guest_list[-1] = 'araba'

# New Guest List 
print(guest_list)
print("\nThis is our new list ", guest_list)

# New invitation message
first_message = "Congrats"
second_message = "you are are invited to my birthday party."

# New guests
first_guest = guest_list[0]
second_guest = guest_list[1]
third_guest = guest_list[2]

# New invitation to guests
print('New Invitation Letters')
print(first_message, first_guest.title(), second_message)
print(first_message, second_guest.title(), second_message)
print(first_message, third_guest.title(), second_message)


# More GUest to the list 
print('\nBIGGER TABLE')
print("\nAttentions everyone we have a bigger table hence we are adding more guests.")

guest_list.insert(0, 'michael')
guest_list.insert(2, 'elizabeth')
guest_list.insert(4, 'ziggy')
guest_list.append('basty')

print('\nNew guest list')
print(guest_list)

# New Invitation List for guest
print("\nBelow is the new guest list.")

# New guest list 
first_guest = guest_list[0]
second_guest = guest_list[1]
third_guest = guest_list[2]
fourth_guest = guest_list[3]
fifth_guest = guest_list[4]
six_guest = guest_list[5]
seventh_guest = guest_list[6]

# New invitation letters to new guests.
print("\nNew guest list...")
print(first_message, first_guest.title(), second_message)
print(first_message, second_guest.title(), second_message)
print(first_message, third_guest.title(), second_message)
print(first_message, fourth_guest.title(), second_message)
print(first_message, fifth_guest.title(), second_message)
print(first_message, six_guest.title(), second_message)
print(first_message, seventh_guest.title(), second_message)



# Shrink Guest List
sorry_message = "we are sorry we have only two tables left."

print('Shrink Guest List')

# Pop out a guest and tell them you have only two chairs.
print('Popping out guests and telling them you are sorry the tables are filled.')


# Dropped guest
first_popped_guest = guest_list.pop(6)
second_popped_guest = guest_list.pop(5)
third_popped_guest = guest_list.pop(4)
fourth_popped_guest = guest_list.pop(3)
fifth_popped_guest = guest_list.pop(2)

# Sorry message to our old guests
print("\nSorry message to our dropped guests")
print(first_popped_guest, sorry_message)
print(second_popped_guest, sorry_message)
print(third_popped_guest, sorry_message)
print(fourth_popped_guest, sorry_message)
print(fifth_popped_guest, sorry_message)

# Invitation to the remaining two guests
print(first_guest.title(), "your invite is still intact.")
print(second_guest.title(), "your invite is still intact.")

# Use del statement to delete remaining guests.

print(guest_list)

del guest_list[0]
print(guest_list)

del guest_list[0]
print(guest_list)