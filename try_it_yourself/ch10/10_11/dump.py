''' Favorite Number: 
- Write a program that prompts for the user’s favorite number. 
- Use json.dump() to store this number in a file. 
- Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”
'''
import json
import math

fileName = 'try_it_yourself/ch10/10_11/fav_num.json'

fav_num = int(input('\nYour fav number: '))

if math.isnan(fav_num):
    print('\n* Invalid value')

with open(fileName, 'w') as f:
    json.dump(fav_num, f)
