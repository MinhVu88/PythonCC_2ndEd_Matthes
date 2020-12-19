# modifying a list in a function
'''
- When you pass a list to a function, the function can modify the list
- Any changes made to the list inside the function’s body are permanent, 
  allowing you to work efficiently even when you’re dealing with large amounts of data
'''

'''
- Consider a company that creates 3D printed models of designs that users submit. 
- Designs that need to be printed are stored in a list & after being printed they’re moved to a separate list. 
- The following code does this without using functions:
'''
unprinted_designs_0 = ['phone case', 'robot pendant', 'dodecahedron']

print('\nThe unprinted designs: ')

for unprinted in unprinted_designs_0: print(f'\n\t- {unprinted}')

completed_models_0 = []

while unprinted_designs_0:
    current_design = unprinted_designs_0.pop()

    print(f'\n+ Printing {current_design}')

    completed_models_0.append(current_design)

print('\nThe completed models:')
for completed in completed_models_0: print(f'\n\t* {completed}')

print('\n--------------------------------------\n')

# with using functions
unprinted_designs_1 = ['labyrinth gift box', 'self-watering planter', 'pop up square basket']

print('The unprinted designs: ')

for unprinted in unprinted_designs_1: print(f'\n\t- {unprinted}')

completed_models_1 = []

def print_models(unprinted, completed):
    while unprinted:
        current_design = unprinted.pop()

        print(f'\n+ Printing {current_design}')
    
        completed.append(current_design)

def show_completed_models(models):
    for model in models: print(f'\n\t* {model}')

print_models(unprinted_designs_1, completed_models_1)

show_completed_models(completed_models_1)

print('\nThe current unprinted_designs_1 list:')

for unprinted in unprinted_designs_1: print(f'\n\t-> {unprinted}')

print('\n--------------------------------------\n')

# preventing a function from modifying a list
'''
- You can address this issue by passing the function a copy of the list, not the original. 
- Any changes the function makes to the list will affect only the copy, leaving the original list intact.
- You can send a copy of a list to a function like this:    function_name(list_name[:])
- The slice notation [:] makes a copy of the list to send to the function
'''
unprinted_designs_2 = ['Toothpaste Tube Squeezer', 'Stackable Hex Drawers', 'Card Deck Shuffler']

print('The unprinted designs: ')

for unprinted in unprinted_designs_1: print(f'\n\t- {unprinted}')

completed_models_2 = []

def print_models(unprinted, completed):
    while unprinted:
        current_design = unprinted.pop()

        print(f'\n+ Printing {current_design}')
    
        completed.append(current_design)

def show_completed_models(models):
    for model in models: print(f'\n\t* {model}')

print_models(unprinted_designs_2[:], completed_models_2)

show_completed_models(completed_models_2)

print('\nThe current unprinted_designs_2 list:')

for unprinted in unprinted_designs_2: print(f'\n\t-> {unprinted}')
