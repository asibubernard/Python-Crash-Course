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


user_profile = build_profile('Ebo', 'Asibu', 
                             29, location='Berlin', 
                             field='Programming', 
                             net_worth='$1 Billion')
print(user_profile)



