# use a for loop to print out each name in a list of magicians
magicians = ['harry houdini', 'david blaine', 'penn & teller', 'jerry sadowitz', 'ricky jay']

for magician in magicians:
    print(f'{magician.title()}, that was a great trick')

    print(f'Do you have anything else up your sleeve, {magician.title()} ?\n')

print('\n\tThank you for coming to the show tonight!')