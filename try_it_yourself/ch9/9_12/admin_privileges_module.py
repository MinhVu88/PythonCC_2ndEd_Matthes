from user_module import User

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