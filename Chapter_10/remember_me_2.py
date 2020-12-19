'''
- Often, you’ll come to a point where your code will work but you’ll recognize that you could improve the code by 
  breaking it up into a series of functions that have specific jobs. 

- This process is called refactoring.

- Refactoring makes your code cleaner, easier to understand and easier to extend.

- We can refactor remember_me_2.py by moving the bulk of its logic into 1 or more functions

- Each function in this final version of remember_me_2.py has a single, clear purpose. 

- We call greet_user() and that function prints an appropriate message: it either welcomes back an existing user or greets a new user. 

- It does this by calling get_stored_username(), which is responsible only for retrieving a stored username if one exists. 

- Finally, greet_user() calls get_new_username() if necessary, which is responsible only for getting a new username and storing it. 

- This compartmentalization of work is an essential part of writing clear code that will be easy to maintain and extend
'''
import json

def get_stored_username():
    """ This function retrieves a stored username & returns the username if it finds one """
    fileName = 'Chapter_10/username_2.json'

    try:
        with open(fileName) as f:
            username = json.load(f)
    except FileNotFoundError:
        # good practice: a function should either return the value you’re expecting or it should return None
        return None 
    else:
        return username

def get_new_username():
    fileName = 'Chapter_10/username_2.json'

    username = input('\nUsername: ')

    with open(fileName, 'w') as f:
        json.dump(username, f)
    
    return username

'''
def greet_user():
    """ This function retrieves a stored username if one exists & prompts for a new username if one doesn’t exist """
    fileName = 'Chapter_10/username_2.json'

    try:
        with open(fileName) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input('\nUsername: ')

        with open(fileName, 'w') as f:
            json.dump(username, f)

            print(f"\n* The username '{username}' is remembered")
    else:
        print(f'\nWelcome back, {username}!')
'''

# the refactored version of the greet_user() function (recommended)
def greet_user():
    username = get_stored_username()

    if username:
        print(f'\nWelcome back, {username}!')
    else:
        username = get_new_username()

        print(f"\n* The username '{username}' is now saved in username_2.json")

greet_user()