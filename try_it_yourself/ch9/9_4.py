''' Number Served: 
- Start with 9_1_2.py 
- Add an attribute called number_served with a default value of 0. 
- Create an instance called restaurant from this class. 
- Print the number of customers the restaurant has served and then change this value and print it again.
- Add a method called set_number_served() that lets you set the number of customers that have been served. 
- Call this method with a new number and print the value again.
- Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
- Call this method with any number you like that could represent how many customers were served in, say, a day of business
'''
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.customer_served = 0
    
    def describe(self):
        print(f'\nThe restaurant is called {self.name} & its cuisine is {self.cuisine}')
    
    def open(self):
        print(f'\n{self.name} is now open')
    
    def set_cust_served(self, cust):
        if cust > self.customer_served:
            self.customer_served = cust
        else:
            print(f'\n* There must be at least 1 customer who eats {self.cuisine}')
    
    def increment_cust_served(self, cust):
        self.customer_served += cust

restaurant = Restaurant("Hell's Kitchen", 'human flesh')

print(f'\nYesterday {restaurant.name} has served {restaurant.customer_served} customer(s)')

restaurant.set_cust_served(0)

restaurant.set_cust_served(7)

print(f'\nToday {restaurant.name} has served {restaurant.customer_served} customer(s)')

restaurant.increment_cust_served(3)

print(f'\nBy the end of today {restaurant.name} has served {restaurant.customer_served} customer(s)')
