''' 9_1) Restaurant: 
- Make a class called Restaurant. 

- The __init__() method for Restaurant should store 2 attributes: a restaurant_name and a cuisine_type. 

- Make a method called describe_restaurant() that prints these 2 pieces of information and 
  a method called open_restaurant() that prints a message indicating that the restaurant is open.

- Make an instance called restaurant from your class. 

- Print the 2 attributes individually and then call both methods
'''
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name

        self.cuisine = cuisine
    
    def describe(self):
        print(f'\nThe restaurant is called {self.name} & its cuisine is {self.cuisine}')
    
    def open(self):
        print(f'\n{self.name} is now open')

restaurant_0 = Restaurant('Ebisu', 'Japanese')
        
restaurant_0.describe()

restaurant_0.open()

''' 9_2) 3 Restaurants: 
- Start with your class from 9_1. 
- Create 3 different instances from the class and call describe_restaurant() for each instance
'''
restaurant_1 = Restaurant('Shamballa', 'Vegetarian')

restaurant_1.describe()

restaurant_1.open()

restaurant_2 = Restaurant('San Fu Lou', 'Cantonese')

restaurant_2.describe()

restaurant_2.open()

restaurant_3 = Restaurant('Noir', 'European')

restaurant_3.describe()

restaurant_3.open()