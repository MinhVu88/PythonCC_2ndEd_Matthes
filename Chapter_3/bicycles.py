# square brackets ([]) indicate a list & individual elements in the list are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print('\nThe bicycles list:\n')

print(bicycles)

print('\n--------------------------------------------------------------\n')

# accessing elements in a list (index positions start at 0, not 1)
print('The item at index #2 in the bicycles list: ' + bicycles[2])

print('The item at index #0 whose 1st letter is capitalized: ' + bicycles[0].title())

print('\n--------------------------------------------------------------\n')

# accessing the last elements in a list by using negative numbers as indices
print('The last item in bicycles: ' + bicycles[-1])

print('The 2nd last item in bicycles: ' + bicycles[-2])

print('The 3rd last item in bicycles: ' + bicycles[-3])

print('\n--------------------------------------------------------------\n')

# use f-strings to create a message based on a value from a list
message = f'My 1st bicycle was a {bicycles[2].title()}'

print(message)
