''' Addition: 
- 1 common problem when prompting for numerical input occurs when people provide text instead of numbers. 
- When you try to convert the input to an int, you’ll get a ValueError. 
- Write a program that prompts for 2 numbers. 
- Add them together and print the result. 
- Catch the ValueError if either input value is not a number and print a friendly error message. 
- Test your program by entering 2 numbers and then by entering some text instead of a number
'''
try:
    val1 = input('\nValue 1: ')

    val2 = input('\nValue 2: ')

    result = int(val1) + int(val2)

    print(result)
except ValueError:
    print('\n* Invalid value(s)\n')
