''' Addition Calculator: 
- Wrap your code from 10_6.py in a while loop so the user can continue entering numbers even if 
  they make a mistake and enter text instead of a number
'''
import math

while True:
    try:
        val1 = input("\nEnter value 1 or 'q' to quit: ")

        if val1 == 'q':
            break

        val2 = input("\nEnter value 2 or 'q' to quit: ")

        if val2 == 'q':
            break

        result = int(val1) + int(val2)
    except ValueError:
        print('\n* Invalid value(s)')
    else:
        print(result)

