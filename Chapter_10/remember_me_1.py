'''
- Combine remember_me_0.py & greet_user.py into 1 file

- When someone runs remember_me_1.py, we want to retrieve their username from memory if possible; 
  therefore, we’ll start with a try block that attempts to recover the username. 
  
- If the file username_1.json doesn’t exist, we’ll have the except block prompt for a username and 
  store it in username_1.json for next time
'''
import json

fileName = 'Chapter_10/username_1.json'

try:
    # If username_1.json exists, we read the username back into memory & print a message welcoming back the user in the else block
    with open(fileName) as f:
        username = json.load(f)
except FileNotFoundError:
    '''
    - If this is the 1st time the user runs the program, username_1.json won’t exist & a FileNotFoundError will occur

    - Python will move on to the except block where we prompt the user to enter their username. 
    
    - We then use json.dump() to store the username and print a greeting

    - Whichever block executes, the result is a username and an appropriate greeting
    '''
    username = input('\nUsername: ')

    with open(fileName, 'w') as f:
        json.dump(username, f)

        print(f"\nYour username '{username}' has been remembered")
else:
    print(f'\nWelcome back, {username}!')