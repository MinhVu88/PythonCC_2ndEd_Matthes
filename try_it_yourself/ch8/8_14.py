''' Cars: 
- Write a function that stores info about a car in a dictionary. 

- The function should always receive a manufacturer and a model name. 

- It should then accept an arbitrary number of keyword arguments. 

- Call the function with the required info and 2 other name-value pairs, 
  such as a color or an optional feature. 
  
- Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)

- Print the dictionary that’s returned to make sure all the info was stored correctly
'''
def make_car(make, model, **info):
    info['make'] = make

    info['model'] = model

    return info

car = make_car('Volkswagen', 'Beetle', color='black', feature='Electronic Stability Control')

for k, v in car.items(): print(f'- {k}: {v}') 
