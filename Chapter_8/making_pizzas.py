'''
# importing an entire module
import pizza_1

pizza_1.make_pizza_1(7, 'pepperoni')

pizza_1.make_pizza_1(18, 'mushrooms', 'green peppers', 'extra cheese')
'''

'''
# importing specific funtions
from pizza_1 import make_pizza_1

make_pizza_1(23, 'pepperoni')

make_pizza_1(51, 'mushrooms', 'green peppers', 'extra cheese')
'''

'''
# using 'as' to give a function an alias
from pizza_1 import make_pizza_1 as mp1

mp1(14, 'pepperoni')

mp1(88, 'mushrooms', 'green peppers', 'extra cheese')
'''

'''
# using 'as' to give a module an alias
import pizza_1 as p1

p1.make_pizza_1(29, 'pepperoni')

p1.make_pizza_1(47, 'mushrooms', 'green peppers', 'extra cheese')
'''

'''
# importing all functions in a module
from pizza_1 import *

make_pizza_1(13, 'pepperoni')

make_pizza_1(27, 'mushrooms', 'green peppers', 'extra cheese')
'''
