def names(filename):
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        pass
        # print("Sorry the file " + filename + " does not exist.")
    else:
        print(content)


filenames = ['text_files/cats.txt', 'dogs.txt']
for filename in filenames:
    names(filename)


