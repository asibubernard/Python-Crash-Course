favorite_languages = {
'jen': [{'name': 'python', 'period': '3months'},
        {'name': 'C++', 'period': '1year'},
        {'name': 'Java', 'period': '10years'}]
}

#print(favorite_languages['jen'][0]['easiest'])
#print(favorite_languages['jen'][1]['hard'])
#print(favorite_languages['jen'][2]['very-hard'])


for name, languages in favorite_languages.items():
    print("\n " + name.title() + ' has loves this programming language; ')

    for language in languages:
        if language['name'] == 'Java':
            print("Man, this the hardest language to learn.")
        else:
            #print(language['name'] + " programming language takes " + language['period'] + " and it not difficult." )
            pass
