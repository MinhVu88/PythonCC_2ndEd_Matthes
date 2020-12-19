class User:
    def __init__(self, first_name, last_name, id):
        self.firstName = first_name
        self.lastName = last_name
        self.id = id
    
    def describe(self): 
        print(f"\n{self.firstName.title()} {self.lastName.title()}'s the web admin & his/her id is {self.id}")