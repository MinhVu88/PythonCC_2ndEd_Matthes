current_users = ['tom', 'harry', 'lucas', 'jessica', 'kate', 'mike']
new_users = ['chester', 'jake', 'lucas', 'andy', 'harry', 'rob']
for user in new_users:
    if user in current_users:
        print('\t' + user.lower() + ' has been used')
    else:
        print(user.lower() + ' is available')