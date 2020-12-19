# a dictionary in a dictionary
users = {'cOmrade': {'first_name': 'jonathan', 
                     'last_name': 'james', 
                     'age': 24}, 
         
         'solo': {'first_name': 'gary', 
                  'last_name': 'mckinnon', 
                  'age': 52}
         }

'''
* the users dictionary:

- keys(dictionaries): cOmrade, solo
- values(keys): first_name, last_name & age

 * the cOmrade & solo dictionaries:
 
 - keys: first_name, last_name & age
 - values: jonathan, james, 24, gary, mckinnon, 52
'''

for username, user_info in users.items():
    print('\nusername: ' + username)
    
    real_name = user_info['first_name'] + ' ' + user_info['last_name']
    age = user_info['age']
    
    print('\treal name: ' + real_name.title())
    print('\tage: ' + str(age))

'''
- username: cOmrade, solo
- user_info: the key-value pairs of cOmrade & solo
'''        