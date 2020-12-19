# passing a list to a function -> the function gets direct access to the contents of the list
def greet_users(names):
    for name in names:
        print(f'\nHello {name.title()}')

usernames = ['maynard keenan', 'adam jones', 'justin chancellor', 'dan carey']

greet_users(usernames)
