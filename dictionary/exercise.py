# Glossary
# favorite_languages = {'kim': 'python', 'julius': 'javascript',
# 'darius': 'kotlin', 'adjetey': 'java'}

# for name, language in favorite_languages.items():
#   if name == 'kim':
#        print(name.title() + " my paddy you for kill " + language.title() +
# "oh...")
#    else:
#        print("\n" + language.title() + " is " + name.title()
#              + "'s favorite programming language.")

# favorite_languages = {
#        'jen': ['python', 'ruby'],
#        'sarah': ['c'],
#        'edward': ['ruby', 'go'],
#        'phil': ['python', 'haskell'],
#        }

# for name, languages in favorite_languages.items():
#    print("\n " + name + " love the following languages")
#    for language in languages:
#        print("\t" + language.title())

pets = [{'kind_of_animal': 'cat', 'owner': 'Johson Nketsia'},
        {'kind_of_animal': 'dog', 'owner': 'Moses Kudozia'}]

for pet in pets:
    print(pet['kind_of_animal'] + " " + pet['owner'])


del pets[1]
pets[0] = {'kind_of_animal': 'lizard', 'owner': 'mozay'}
# pets[1] = {'kind_of_animal': 'mosquitoe', 'owner': 'stanish'}
pets.append({'kind_of_animal': 'mosquitoe', 'owner': 'stanish'})

# update dictionary in list
pets.append({'kind_of_animal': 'yijou', 'owner': 'adfl'})
pets.append({'kind_of_animal': 'athnw', 'owner': 'oiu'})
pets.append({'kind_of_animal': 'you', 'owner': 'adfl'})
pets.append({'kind_of_animal': 'y', 'owner': 'afl'})

for pet in pets:
    print(pet, " pets")

favorite_places = {
        'ebo': {'first_place': 'new york',
                'second_place': 'berlin',
                'third_place': 'toronto'},
        'maame': {'first_place': 'tema',
                  'second_place': 'paris',
                  'third_place': 'madrid'}}

for person, places in favorite_places.items():
    print("\n", person.title(), "favorite places are:")
    best_places = places['first_place'] + ", " + places['second_place'] + ", " + places['third_place']
    print(best_places.title())

