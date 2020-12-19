''' Privileges: 
- Write a separate Privileges class. 
- The class should have 1 attribute, privileges, that stores a list of strings as described in 9_7.py. 
- Move the show_privileges() method to this class. 
- Make a Privileges instance as an attribute in the Admin class. 
- Create a new instance of Admin and use your method to show its privileges
'''
class User:
    def __init__(self, first_name, last_name, id):
        self.firstName = first_name
        self.lastName = last_name
        self.id = id
    
    def describe(self): 
        print(f"\n{self.firstName} {self.lastName}'s the web admin & his/her id is {self.id}")

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

admin = Admin('Paul', 'DAmour', 'Bottom*666*Feeder')

admin.describe()

admin.privilege.show_privileges()
