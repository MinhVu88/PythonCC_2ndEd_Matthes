# moving items in 1 list to another

'''
consider a list of newly registered but unverified users of a website, who are currently in a list of unconfirmed users
use a while loop to move these unverified users out of the list of unconfirmed users as each one is being verified
and then add them to a separate list of confirmed users 
'''

unconfirmed_users = ['maynard', 'justin', 'adam', 'danny']
confirmed_users = []

print ('The following users have not been verified:')
print ('-------------------------------------------')

for unconfirmed_user in unconfirmed_users:
    print ('\n\t- ' + unconfirmed_user.title())

print ('\nThe verifying process now begins:')
print ('---------------------------------')

while unconfirmed_users:
    # use the pop() function to pull each unverified user out of unconfirmed_users & assign them to the confirmed_user variable, 1 by 1
    confirmed_user = unconfirmed_users.pop() 
    
    print (f'\n\t+ {confirmed_user.title()} is being verified')
    
    confirmed_users.append(confirmed_user) # add the verified users to the list of confirmed users

print ('\nThe following users have been verified:')
print ('---------------------------------------')

for verified_user in confirmed_users:
    print ('\n\t* ' + verified_user.title())