class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name

        self.cuisine = cuisine
    
    def describe(self):
        print(f'\nThe restaurant is called {self.name.title()} & its cuisine is {self.cuisine}')
    
    def open(self):
        print(f'\n{self.name} is now open')