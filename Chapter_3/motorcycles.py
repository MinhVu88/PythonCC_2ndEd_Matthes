# modifying elements in a list
motorcycles_0 = ['honda', 'yamaha', 'suzuki']

print('\nThe motorcycles_0 list:')

print(motorcycles_0)

motorcycles_0[0] = 'ducati'

print("\nThe value of the motorcycles_0's item #0 has been changed:")

print(motorcycles_0)

print('\n--------------------------------------------------------------')

# appending elements to the end of a list by using the append() method
motorcycles_0.append('honda')

print('\nhonda is appended to the end of motorcycles_0:')

print(motorcycles_0)

motorcycles_1 = []

motorcycles_1.append('Harley-Davidson')

motorcycles_1.append('Kawasaki')

motorcycles_1.append('Triumph')

print('\nItems are appended to the empty motorcycles_1 list:')

print(motorcycles_1)

print('\n--------------------------------------------------------------')

# inserting elements into a list by using the insert() method
motorcycles_1.insert(0, 'aprilia')

print('\nA new item is inserted into motorcycles_1:')

print(motorcycles_1)

print('\n--------------------------------------------------------------')

# removing an element by using the del statement
del motorcycles_1[2]

print('\nmotorcycles_1 with its item #2 removed:')

print(motorcycles_1)

# removing an item & then using it in some way by applying the pop() method
print('\nThe last item in the motorcycles_0 list: ' + motorcycles_0.pop())

print('\nThe 2nd item in motorcycles_1: ' + motorcycles_1.pop(1))

print('\n')

# removing an item by its value & then using it in some way by applying the remove() method
print(motorcycles_0)

removedItem = 'suzuki'

motorcycles_0.remove(removedItem)

print(f'{removedItem.title()} is removed from motorcycles_0')

print(motorcycles_0)

