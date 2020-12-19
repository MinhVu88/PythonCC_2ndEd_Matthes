requested_toppings_0 = ['extra cheese', 'sausage', 'pepperoni', 'onion']

for topping in requested_toppings_0:
    print('adding ' + topping)

print('\nfinish making your pizza')

print('\n')

# what if sausages are unavailable?
for topping in requested_toppings_0:
    if topping == 'sausage':
        print('\tSorry, ' + topping + ' is unavailable for now')
    else:
        print('adding ' + topping)

print('\nfinish making your pizza')

print('\n')

# check if a list is not empty
''' 
When the name of a list is used in an if statement, Python returns True if the list contains at least 1 item 
An empty list evaluates to False  
'''
requested_toppings_1 = []

if requested_toppings_1:
    for topping in requested_toppings_1:
        print('adding ' + topping)
    print('\nfinish making your pizza')
else:
    print('are you sure you want a plain pizza?') 

print('\n')

# use multiple lists
available_toppings = ['spinarch', 'pepperoni', 'bacon', 'black olives', 'green peppers', 'pineapples', 'extra cheese']
requested_toppings_2 = ['spinarch', 'pepperoni', 'cigarette butt']

for requested_topping in requested_toppings_2:
    if requested_topping in available_toppings:
        print('adding ' + requested_topping)
    else:
        print('\tsorry, we do not have ' + requested_topping + ' as a pizza topping here')

print('\nfinish making your pizza')













