''' 
- Python allows a function to collect an arbitrary number of arguments from the calling statement
- The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings 
  and pack whatever values it receives into this tuple
'''
def make_pizza_0(*toppings):
    print('\nMaking a pizza with the following toppings:')

    for topping in toppings: print(f'\n- {topping}')

make_pizza_0('pepperoni')

make_pizza_0('mushrooms', 'green peppers', 'extra cheese')

print('\n--------------------------------------\n')

'''
- If you want a function to accept several different kinds of arguments, 
  the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. 
- Python matches positional & keyword arguments 1st & then collects any remaining arguments in the final parameter
'''
def make_pizza_1(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following toppings:')

    for topping in toppings: print(f'\n- {topping}')

make_pizza_1(23, 'pepperoni')

make_pizza_1(51, 'mushrooms', 'green peppers', 'extra cheese')
