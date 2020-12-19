alien_0 = {'color': 'red',
           'points': 7}  # keys: color & points - values: red & 5

print(alien_0['color'])

print(alien_0['points'])

print('\n')

# access values in a dic
new_points = alien_0['points']

print("you've just shot down an alien & thus earned " + str(new_points) + ' points')

print('\n')

# add new key-value pairs
alien_1 = {'color': 'white',
           'points': 13}

print(alien_1)

alien_1['x_position'] = 0  # a new key-value pair

alien_1['y_position'] = 47

print(alien_1)

print('\n')

# start with an empty dic & add new key-value pairs to it
alien_2 = {}

alien_2['color'] = 'black'

alien_2['points'] = 69

print(alien_2)

print('\n')

# modify values in a dic
alien_3 = {'color': 'yellow', 
           'points': 21}

print('the alien is ' + alien_3['color'])

alien_3['color'] = 'purple'

print('the alien now is ' + alien_3['color'])

print('\n')

# a more interesting example of modifying values in a dic
alien_4 = {'x_position': 0, 
           'y_position': 18, 
           'speed': 'pretty fast'}

print('the original x_position: ' + str(alien_4['x_position']))

if alien_4['speed'] == 'slow':
    x_position_increment = 5
elif alien_4['speed'] == 'medium':
    x_position_increment = 10
else:
    x_position_increment = 20

print('\tthe current x_position_increment: ' + str(x_position_increment))

alien_4['x_position'] += x_position_increment

print('the new x_position: ' + str(alien_4['x_position']))

alien_4['speed'] = 'slow'

if alien_4['speed'] == 'slow':
    x_position_increment = 5
elif alien_4['speed'] == 'medium':
    x_position_increment = 10
else:
    x_position_increment = 20

print('\tthe new x_position_increment: ' + str(x_position_increment))

alien_4['x_position'] += x_position_increment

print('the latest x_position: ' + str(alien_4['x_position']))

print('\n')

# permanently remove key-value pairs by using the del statement
alien_5 = {'color': 'green',
           'points': 25}

print(alien_5)

del alien_5['points']

print(alien_5)