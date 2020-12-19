#  a list of dictionaries
alien_0 = {'name': 'paul',
           'age': 12}

alien_1 = {'name': 'luke',
           'age':18}

alien_2 = {'name': 'jake',
           'age': 25}

aliens_0 = [alien_0, alien_1, alien_2]

for alien in aliens_0:
    print(alien)

print('\n')

aliens_1 = []

for alien_number in range(10):
    new_alien = {'color': 'white', 
                 'points': 5, 
                 'speed': 'slow'} # create a dictionary which contains various pieces of info about an alien
    aliens_1.append(new_alien) # add the dictionary to the aliens_1 list

print('the 1st 6 aliens_1:\n')

for alien in aliens_1[:6]:
    print(alien)

print('\n-----')
print('\n\tthe total number of aliens_1: ' + str(len(aliens_1)))

print('\n')

# change the colors, points & speed of the 1st 3 aliens_1
for alien in aliens_1[:3]:
    if alien['color'] == 'white':
        alien['color'] = 'black'
        alien['points'] = 10
        alien['speed'] = 'medium'

print('the modified version of the 1st 3 aliens_1:\n')

for alien in aliens_1[:6]:
    print(alien)

print('\nanother modified version of the 1st 3 aliens_1:\n')

for alien in aliens_1[:3]:
    if alien['color'] == 'white':
        alien['color'] = 'black'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'black':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens_1[:6]:
    print(alien)