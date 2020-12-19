# a tuple is a list that contains immutable items (items that can't change)
rectangle_dimensions = (200, 50)

print(rectangle_dimensions[0])

print(rectangle_dimensions[1])

'''
# try changing 1 of the items (doesn't work)
rectangle_dimensions[0] = 300

print(rectangle_dimensions[0])
'''

print('\n')

# although you can't modify a tuple, you can assign a new value to a variable that holds a tuple
print('Original dimensions:')

for dimension in rectangle_dimensions:
    print(dimension)

rectangle_dimensions = (300, 100)

print('\nModified dimensions:')

for dimension in rectangle_dimensions:
    print(dimension)