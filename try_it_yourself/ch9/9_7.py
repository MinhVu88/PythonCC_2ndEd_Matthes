''' Admin: 
- An administrator is a special kind of user. 
- Write a class called Admin that inherits from the User class in 9_3.py or 9_5.py 
- Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user" and so on. 
- Write a method called show_privileges() that lists the administrator’s set of privileges. 
- Create an instance of Admin and call your method
'''
class User:
    def __init__(self, first_name, last_name, id):
        self.firstName = first_name
        self.lastName = last_name
        self.id = id
    
    def describe(self): 
        print(f"\n{self.firstName} {self.lastName}'s the web admin & his/her id is {self.id}")

class Admin(User):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id)

        self.privileges = ['add posts', 'delete posts', 'ban users', 
                           'approve/reject comments', 
                           'create & manage content types/categories/filters', 
                           'set default configurations for page-level components',
                           "Revoke a person's role as Website Administrator", 
                           'Select the security group types']
    
    def show_privileges(self):
        for p in self.privileges:
            print(f'\n\t* {p}')

admin = Admin('Adam', 'Jones', 'Bastardometer#666')

admin.describe()

print("\nThe following are the admin's privileges:")

admin.show_privileges()