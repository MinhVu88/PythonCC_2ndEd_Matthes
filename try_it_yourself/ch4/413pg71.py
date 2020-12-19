buffet = ('chicken rice', 'noodle', 'bread', 'beef', 'pork')
for food in buffet:
    print(food)

'''
buffet[2] = 'lamb chop'
print(buffet[2])
'''

print('\n')

print('Original menu:')
for food in buffet:
    print('\t' + food)
print('\nNew menu:')
buffet = ('chicken rice', 'noodle', 'soup', 'beef', 'lamb chop')
for food in buffet:
    print('\t' + food)