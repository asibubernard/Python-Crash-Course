# Print content by reading entire file.
with open('learning_python.txt') as file_object:
    content = file_object.read()
    print(content)


# Looping over the file object
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())


# Store lines in a list and use outside WITH block
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

learning_python = ''
for line in lines:
    learning_python += line

print(learning_python)

# Replacing a word in string with replace() method
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

learning_python = '' 
for line in lines:
    learning_python += line.replace('Python', 'C')

print(learning_python)

