family = {
    'father': [{"name": 'Ebo', 'age': 23, 'education': 'Graduate'}, 
               {"name": 'Ato', 'age': 43, 'education': 'Ph.D'},
               {'name': "Archie", 'age': 12, 'education': 'Bachelor'}],
    'mother': {'first_name': 'Elizabeth', 'last_name': 'Asibu'}    
}

new_family = {
    'father': [{"name": 'Bo', 'age': 3, 'Education': 'FRadduate'},
               {"name": 'to', 'age': 3, 'Education': 'Ph.D'},
               {'name': "achie", 'age': 2, 'Education': 'Bachelor'}],
    'mother': {'first_name': 'Elizabeth', 'last_name': 'Asibu'} 
}


# print(family['father'][0])
old_children = family['father']
new_children = new_family['father']

children = {}

# print("Old children of Michael...")
# for child in old_children:

#     if child.items():
#         for key, value in child.items():
#             print(key, value)
#            #setattr(children, keys(), values()) 

# print(old_children, "Old children")
# print("\n", new_children, "New children")

# print("\nUpdating old children names...")


#for i in range(0, len(new_children)):
   # new_child = new_children[i]
   # print(new_child)
   # if new_child.items():
       # for key, value in list(new_child[i].items()):
           # print(key, value)
        #setattr(old_children, key, value)
           # old_children[key] = value


for key, value in list(new_children.items()):
    print(key, value)
    setattr(old_children, key, value)

#print(old_children)
