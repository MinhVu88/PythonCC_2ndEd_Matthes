''' Ice Cream Stand: 
- An ice cream stand is a specific kind of restaurant. 
- Write a class called IceCreamStand that inherits from the Restaurant class 
  in 9_1_2.py or 9_4.py 
- Either version of the class will work; just pick the one you like better.
- Add an attribute called flavors that stores a list of ice cream flavors. 
- Write a method that displays these flavors. 
- Create an instance of IceCreamStand and call this method
'''
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name

        self.cuisine = cuisine
    
    def describe(self):
        print(f'\nThe restaurant is called {self.name} & its cuisine is {self.cuisine}')
    
    def open(self):
        print(f'\n{self.name} is now open')

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)

        self.flavors = []
    
    def display_flavors(self):
        for f in self.flavors:
            print(f'\n* {f}-flavored ice cream')

iceCream = IceCreamStand('Haagen Dazs', 'ice cream')

iceCream.describe()

iceCream.flavors = ['strawberry', 'vanilla', 'strawberry cheese cake', 'macadamia nut', 'green tea']

iceCream.display_flavors()
