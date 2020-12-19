''' Login Attempts: 
- Add an attribute called login_attempts to 9_3.py 
- Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
- Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
- Make an instance of the User class and call increment_login_attempts() several times.
- Print the value of login_attempts to make sure it was incremented properly and then call reset_login_attempts(). 
- Print login_attempts again to make sure it was reset to 0
'''
class User:
    def __init__(self, first_name, last_name, id):
        self.firstName = first_name
        self.lastName = last_name
        self.id = id
        self.login_attempts = 0
    
    def describe(self): 
        print(f"\n{self.firstName} {self.lastName}'s id is {self.id} ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0    
    
    def greet(self): print(f'\nHello {self.firstName} {self.lastName}')

user = User('Danny', 'Carey', 'Membranophones#666')

user.increment_login_attempts()

user.increment_login_attempts()

user.increment_login_attempts()

print(f"\n{user.firstName} {user.lastName}'s login attempts so far are {user.login_attempts}")

user.reset_login_attempts()

print(f"\n{user.firstName} {user.lastName}'s login attempts after resetting are {user.login_attempts}")
