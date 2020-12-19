fav_numbers = {'jake': 47, 
               'liam': 18, 
               'colin': 25, 
               'sarah': 69, 
               'kate':13 }

friends = ['paul', 'colin', 'jessica', 'kate', 'justin']

for name, no in fav_numbers.items():
    if name not in friends:
        print('hi ' + name.title() + ', you like ' + str(no) + ', right?')
    else:
        print('-  ' + name.title() + " is in friends & his/her fav number is " + str(no))

for friend in friends:
    if friend in fav_numbers.keys():
        print('\nhi ' + friend.title() + ', i already know your fav number')
    else:
        print('\n' + friend.title() + ', plz choose your fav number')     