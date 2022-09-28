from users import User
from admin import Privileges, Administrator


admin = Administrator('ato', 'doe', 27)
print(admin.first_name.title() + ' ' + admin.last_name.title() + 
      ' is the new admin and is  ' + str(admin.age) + ' years old.')
admin.privileges.show_privileges()
