name_0 = input('enter your name: ')

print(f'\nHi {name_0.title()}')

print('\n')

prompt = 'if you tell us more about yourself, we then can personalize the messages you see. '
prompt += "\nwhat's your full name? "

name_1 = input(prompt)

print(f'\nHello {name_1.title()}')

print('\n')
 
# when you use the input() function, python interprets everything the user enters as a string
# use the int() function to convert the string input to an integer value

age = input('enter your current age: ')

new_age = int(age) + 1

print (f"next year you'll be {str(new_age)} years old")