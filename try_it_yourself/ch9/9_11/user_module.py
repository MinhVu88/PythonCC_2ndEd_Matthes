''' Imported Admin: 
- Start with your work 9_8.py 
- Store the classes User, Privileges and Admin in 1 module. 
- Create a separate file, make an Admin instance and call show_privileges() to show that everything is working correctly
'''
class User:
    def __init__(self, first_name, last_name, id):
        self.firstName = first_name
        self.lastName = last_name
        self.id = id
    
    def describe(self): 
        print(f"\n{self.firstName.title()} {self.lastName.title()}'s the web admin & his/her id is {self.id}")

class Privileges:
    def __init__(self):
        self.privileges = ['add posts', 'delete posts', 'ban users', 
                           'approve/reject comments', 
                           'create & manage content types/categories/filters', 
                           'set default configurations for page-level components',
                           "Revoke a person's role as Website Administrator", 
                           'Select the security group types']
    
    def show_privileges(self):
        for p in self.privileges:
            print(f'\n\t* {p}')

class Admin(User):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id)
        self.privilege = Privileges()