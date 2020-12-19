# sorting a list permanently alphabetically with the sort() method
cars_0 = ['BMW', 'Audi', 'Toyota', 'Subaru']

print(cars_0)

cars_0.sort()

print(cars_0)

# sorting a list permanently alphabetically in reverse order by passing 'reverse=true' to sort()
cars_0.sort(reverse=True)

print(cars_0)

print('\n--------------------------------------------------------------\n')

# sorting a list temporarily with the sorted() function
cars_1 = ['Tesla', 'Rolls Royce', 'Lamborghini', 'Volkswagen', 'Maybach']

print('The original cars_1:')

print(cars_1)

print('\nThe sorted cars_1:')

print(sorted(cars_1))

print('\nBack to the original order:')

print(cars_1)

print('\n--------------------------------------------------------------\n')

# To reverse the original order of a list, use the reverse() method, NOT in alphabetical order
cars_2 = ['Bentley', 'Chrysler', 'Aston Martin', 'Ferrari', 'Daimler AG']

print(cars_2)

cars_2.reverse()

print(cars_2)

cars_2.reverse()

print(cars_2)

print('\n--------------------------------------------------------------\n')

length = len(cars_2)

print(f'The length of cars_2: {length}') # use the len() function to find the length of a list

