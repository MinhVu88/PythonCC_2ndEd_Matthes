''' Multiple Modules: 
- Store the User class in 1 module and store the Privileges and Admin classes in a separate module. 
- In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly
'''
from user_module import User as u
from admin_privileges_module import Admin as a, Privileges as p

admin = a('maynard', 'keenan', 'Möstresticator#666')

admin.describe()

admin.privilege.show_privileges()
