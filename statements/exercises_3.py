# Hello Admin
#users = ['ebo', 'ato', 'maame']

#for user in users:
   # if user == 'admin':
       # print("Hello admin, would you like to see a status report?")
   # else:
       # print("Hello " + user + ", you are welcome")


# No users 
#users_empty = []
#if user not in users_empty:
   # print("There are no users")


# Checking Usernames
current_users = ['ebo', 'ato', 'maame', 'admin', 'archie', 'daa', 'mum']
new_users = ['jenny', 'mary', 'wendel', 'Ato', 'ARCHIE']


for username in new_users:
    new_username = username.lower() 
    if new_username in current_users: 
        print("Username is taken, you need to pick another username")
    else:
        print("Username is available")

# Ordinal Numbers
ordinal_numbers = [1, 2, 3, 5, 6, 7, 8, 9]

for number in ordinal_numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")

