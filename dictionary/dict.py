favorite_languages = {
    'jen': [{'name': 'python', 'period': '3 months'},
            {'name': 'C++', 'period': '1 year'},
            {'name': 'Java', 'period': '10 years'}]}

# print(favorite_languages['jen'][0]['easiest'])
# print(favorite_languages['jen'][1]['hard'])
# print(favorite_languages['jen'][2]['very-hard'])


for name, languages in favorite_languages.items():
    print("\n" + name.title() + ' has loves this programming language; ')

    for language in languages:
        print('\n' + language['name'].title() + " " + language['period'])


