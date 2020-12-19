class Car_0:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_name(self):
        return f'\n{self.year} {self.make.title()} {self.model.title()}'

print(Car_0('tesla', 'model x', 2019).get_name())

'''
- When an instance is created, attributes can be defined without being passed in as parameters 

- These attributes can be defined in the __init__() method, where they are assigned a default value

- Let’s add an attribute called odometer_reading that always starts with a value of 0 

- We’ll also add a method read_odometer() that helps us read each car’s odometer

- This time when Python calls the __init__() method to create a new instance, 
  it stores the make, model and year values as attributes like it did in the previous example 

- Then Python creates a new attribute called odometer_reading and sets its initial value to 0 

- We also have a new method called read_odometer() that makes it easy to read a car’s mileage
'''
class Car_1:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # a default value
    
    def get_name(self):
        return f'\n{self.year} {self.make.title()} {self.model.title()}'
    
    def read_odometer(self):
        return f'\nThis {self.model.title()} {self.make.title()} has {self.odometer_reading} miles on it'
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\n\tYou can't roll back an odometer")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

print(Car_1('lamborghini', 'aventador', 2019).read_odometer())

# modifying an attribute's value directly thru an instance
car0 = Car_1('volkswagen', 'beetle', 2019)

car0.odometer_reading = 23

print(car0.read_odometer())

# modifying an attribute's value thru a method
car1 = Car_1('mercedes-benz', 'maybach', 2019)

car1.update_odometer(7)

print(car1.read_odometer())

car2 = Car_1('porsche', '718 spyder', 2019)

car2.update_odometer(-3)

# incrementing an attribute's value thru a method
car3 = Car_1('subaru', 'outback', 2015)

print(car3.get_name())

car3.update_odometer(23_500)

print(car3.read_odometer())

car3.increment_odometer(100)

print(car3.read_odometer())
