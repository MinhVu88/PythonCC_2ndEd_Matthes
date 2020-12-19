''' Users: 
- Make a class called User. 

- Create 2 attributes called first_name and last_name and 
  then create several other attributes that are typically stored in a user profile. 

- Make a method called describe_user() that prints a summary of the user’s information. 

- Make another method called greet_user() that prints a personalized greeting to the user.

- Create several instances representing different users and call both methods for each user
'''
class User:
    def __init__(self, first_name, last_name, age, job):
        self.firstName = first_name
        self.lastName = last_name
        self.age = age
        self.job = job
    
    def describe(self): 
        print(f'\n{self.firstName} {self.lastName} is {self.age} years old & he/she is a {self.job}')
    
    def greet(self): print(f'\nHello {self.firstName} {self.lastName}')

user0 = User('Maynard', 'Keenan', 55, 'wine maker')

user0.greet()

user0.describe()

user1 = User('Adam', 'Jones', 54, 'guitarist')

user1.greet()

user1.describe()
