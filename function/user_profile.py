""" Using Arbitrary Keyword Arguments"""

def build_profile(first, last, age, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    profile['age'] = age
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', '29',
                              location='prince', field='physics')

print(user_profile)


def list_family(dad, *siblings):
    family = []
    family.append(dad)
    for sibling in siblings:
        family.append(sibling)

    return family


asibu_family = list_family('Michael', 'Elizabeth',
                           'Sophia', 'Richard', 'Moses')
print(asibu_family)
