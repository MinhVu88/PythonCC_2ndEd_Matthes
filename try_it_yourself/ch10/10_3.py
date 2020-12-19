''' Guest: 
- Write a program that prompts the user for their name. 
- When they respond, write their name to a file called guest.txt
'''
fileName = 'try_it_yourself/ch10/guest.txt'

name = input('\nYour name: ')

with open(fileName, 'w') as file_object:
    file_object.write(name)
