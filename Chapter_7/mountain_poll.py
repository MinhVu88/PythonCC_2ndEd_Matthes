# filling a dictionary with user input
poll_results = {}
poll_is_active = True

while poll_is_active:
    # get user input which includes names & replies
    name = input('\nYour name: ')
    reply = input('\nWhat mountain would you like to climb? ')
    
    poll_results[name] = reply # add names & replies to poll_results as its keys (names) & values (replies)
    
    # ask the user if he/she wants to play again
    poll_again = input('\nWould you like to take another poll? (yes/no) - ')
    
    if poll_again == 'no':
        poll_is_active = False

print ('\n-----Poll result-----')
for name, reply in poll_results.items():
    print (f'\n {name.title()} would like to climb {reply.title()} mountain')   
    