# Write to a file

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Append to a file 

with open(filename, 'a') as file_object:
    file_object.write("I also lve finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    print('Done appending text to file_object.')
