''' T-Shirt: 
- Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
- The function should print a sentence summarizing the size of the shirt and the message printed on it.
- Call the function once using positional arguments to make a shirt. 
- Call the function a 2nd time using keyword arguments
'''
def make_shirt(size, message):
    print(f"\nThis's a {size}-size T-shirt with a message on it saying '{message}'")

make_shirt('XL', 'Apply Yourself!') # positional arguments

make_shirt(message='Our Business Is Life Itself', size='L') # keyword arguments
