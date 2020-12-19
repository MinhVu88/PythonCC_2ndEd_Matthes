'''
- When calling a function, Python must match each argument in the function call with a parameter in the function definition
- Values matched up this way are called positional arguments
'''
def describe_pet_0(type, name):
    print(f'\nI have a {type} & its name is {name}')

describe_pet_0('Siberian husky', 'Sumo')

describe_pet_0('hamster', 'Pettigrew')

# make sure the order of the arguments in a function call matches the order of the parameters in the function’s definition
describe_pet_0('Tom', 'cat')

'''
- A keyword argument is a name-value pair that you pass to a function
- Keyword arguments free you from having to worry about correctly ordering your arguments in the function call 
  and they clarify the role of each value in the function call
'''
describe_pet_0(name='Laika', type='Soviet space dog')

# default values
# For example, if most calls to descrive_pet_1 are used to describe dogs, you can set the default value of 'type' to 'dog'
''' Note:
- Because the default value makes it unnecessary to specify a type of animal as an argument, 
  the only argument left in the function call is the pet’s name

- Python still interprets this as a positional argument

- So if the function is called with just a pet’s name, 
  that argument will match up with the 1st parameter listed in the function’s definition

- This is the reason the 1st parameter needs to be 'name'
'''
def describe_pet_1(name, type='dog'):
    print(f'\nI have a {type} & its name is {name}')

# now anyone calling this function can omit the 'type' argument as python knows to use the default param
describe_pet_1(name='Hachiko')

describe_pet_1('Blondi') # another way to call this function

describe_pet_1(name='Hissy', type='Burmese python') # override the default value

describe_pet_1() # causes an error
