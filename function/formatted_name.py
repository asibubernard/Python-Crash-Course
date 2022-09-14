""" Returning a simple value """

def get_formatted_name(first_name, last_name, middle_name=""):
    """ Return a full name, neatly formatted with an optional argument """
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name +  " " + last_name
    return full_name.title()

musician = get_formatted_name('ebo', 'asibu')
musician = get_formatted_name('ebo', 'yarteh', 'asibu')
print(musician)

