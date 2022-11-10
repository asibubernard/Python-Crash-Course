"""Accessing last four items in a list of dictionaries."""

restaurants = [{'name': 'Green Land'}, {'name': 'Mawusi'}, {'name': 'Koowa'},
               {'name': 'Bushira'}, {'name': 'Maame Ekua'}, {'name': 'Naana'}]

for restaurant in restaurants[-4:]:
    print(restaurant)

