poll_results = {}
poll_is_active = True

while poll_is_active:
    name = input('\nyour name: ')
    reply = input('\nwhat is your dream vacation? ')
    
    poll_results[name] = reply
    
    again = input('\nwould you like to let someone else pick their dream vacations? (yes/no) - ')
    if again != 'yes':
        poll_is_active = False
    

print ('\n-----Poll result-----')
for name, reply in poll_results.items():
    print ('\n' + name.title() + ' would like to travel to ' + reply.title())