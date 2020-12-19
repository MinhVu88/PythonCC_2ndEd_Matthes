''' Verify User: 
- remember_me_2.py in Chapter_10 assumes either that the user has already entered their username or 
  that the program is running for the 1st time. 
- We should modify it in case the current user is not the person who last used the program.
- Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 
- If it’s not, call get_new_username() to get the correct username
'''
import json

def get_stored_username():
    fileName = 'try_it_yourself/ch10/10_13/username.json'

    try:
        with open(fileName) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None 
    else:
        return username

def get_new_username():
    fileName = 'try_it_yourself/ch10/10_13/username.json'

    username = input('\nUsername: ')

    with open(fileName, 'w') as f:
        json.dump(username, f)
    
    return username

def greet_user():
    username = get_stored_username()

    reply = input(f"\n* Is the username '{username}' yours? (y/n) -> ")

    if reply == 'y':
        print(f'\nWelcome back, {username}!')
    else:
        username = get_new_username()

        print(f"\n* The username '{username}' is now saved in username.json")

greet_user()