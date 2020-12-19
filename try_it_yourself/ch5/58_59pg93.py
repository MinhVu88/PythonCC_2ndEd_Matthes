usernames_0 = ['keith', 'brad', 'pauline', 'admin', 'ford', 'macy', 'lauren']

for name in usernames_0:
    if name == 'admin':
        print('\tHello ' + name.title() + ', would you like to see the status report?')
    else:
        print('Hi ' + name.title() + ', thanks for logging in again')

print('\n')

usernames_1 = []

if usernames_1:
    for name in usernames_1:
        print('Hi ' + name.title())
else:
    print('We need to find some users')