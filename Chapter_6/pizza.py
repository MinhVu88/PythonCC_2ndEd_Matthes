# a list in a dictionary
pizza = { 'crust': 'thick', 
         'toppings': ['pepperoni', 'extra cheese', 'black olives']}

print('a pizza with a ' + pizza['crust'] + ' crust & the following toppings have been ordered:')

for topping in pizza['toppings']:
    print('- ' + topping.title())