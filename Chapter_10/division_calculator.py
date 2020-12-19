#print(5 / 0) # raise the ZeroDivisionError exception

# use a try-except block
try:
    print(5 / 0)
except ZeroDivisionError:
    print("\nYou can't divide by zero!")

print('\n------------------------------')

# use a try-except-else block to prevent program crashes
'''
- The try-except-else block works like this: Python attempts to run the code in the try block. 

- The only code that should go in a try block is code that might cause an exception to be raised. 

- Sometimes you’ll have additional code that should run only if the try block was successful; 
  this code goes in the else block. 

- The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try block
'''
print("\nEnter 2 numbers & divide them or enter 'q' to quit")

while True:
    num1 = input('\n* number 1: ')

    if num1 == 'q':
        break

    num2 = input('\n* number 2: ')

    if num2 == 'q':
        break

    try:
        result = int(num1) / int(num2)
    except ZeroDivisionError:
        print("\nYou can't divide by zero!")
    else:
        print(result)    
    
