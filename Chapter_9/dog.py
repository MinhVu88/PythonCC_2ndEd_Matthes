class Dog:
    """ A simple class that models a real-world dog """
    def __init__(self, name, age):
        """ The __init__() method (a function inside a class) that initializes the name & age attributes """
        """ The self param must be declared 1st in the method definition """
        """ Any self.variable is avail to every class method & accessible thru every class instance """
        self.name = name

        self.age = age
    
    def sit(self):
        """ A method that simulates a dog sitting on command """
        print(f'{self.name}! Sit your drunken ass down')
    
    def roll_over(self):
        """ A method that simulates a dog rolling over on command """
        print(f'{self.name}! Roll over this metal-spike-covered mat')

# create the 1st instance from the Dog class
dog1 = Dog('Sumo', 5)

# access the attributes
print(f'\nMy dog is called {dog1.name} & it is {dog1.age} years old')

# call the methods
dog1.sit()

dog1.roll_over()

# the 2nd instance
dog2 = Dog('Bean', 10)

print(f'\nYour dog is called {dog2.name} & it is {dog2.age} years old')

dog2.sit()

dog2.roll_over()