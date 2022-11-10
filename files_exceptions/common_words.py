# Count the number of time a word appears.

filename = 'text_files/alice.txt'
try:
    with open(filename) as f_object:
        content = f_object.read()
except FileNotFoundError:
    print("Sorry " + filename + " is not available.")
else:
    counts = content.lower().count('alice')
    print(counts)
