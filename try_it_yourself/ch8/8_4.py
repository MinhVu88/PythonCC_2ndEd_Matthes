''' Large Shirts: 
- Modify the make_shirt() function in 8_3.py so that shirts are large by default with a message that reads I love Python. 
- Make a large shirt and a medium shirt with the default message and a shirt of any size with a different message
'''
def make_shirt_1(message, size='L'):
    print(f"\nThis's a {size}-size T-shirt with a message on it saying '{message}'")

make_shirt_1('I love Python')

def make_shirt_2(size, message='I love Java'):
    print(f"\nThis's a {size}-size T-shirt with a message on it saying '{message}'")

make_shirt_2('M')