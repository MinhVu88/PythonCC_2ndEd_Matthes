''' Imported Restaurant: 
- Create a Restaurant class & store it in restaurant_module.py 
- Make a separate file that imports Restaurant. 
- Make a Restaurant instance and call 1 of the class’s methods to show that 
  the import statement is working properly
'''
from restaurant_module import Restaurant

res = Restaurant('Cyberia', 'cafe & drugs')

res.describe()

res.open()
