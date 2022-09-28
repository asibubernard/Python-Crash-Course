"""Using the Python Standard Libary"""
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['esi'] = 'c#'
favorite_languages['ebo'] = 'javascript'
favorite_languages['ben'] = 'ruby'
favorite_languages['mark'] = 'go'
favorite_languages['moses'] = 'c++'
favorite_languages['thomas'] = 'java'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

