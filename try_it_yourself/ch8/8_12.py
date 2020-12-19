''' Sandwiches: 
- Write a function that accepts a list of items a person wants on a sandwich.
- The function should have 1 parameter that collects as many items as the function call provides and 
  it should print a summary of the sandwich that’s being ordered. 
- Call the function 3 times, using a different number of arguments each time
'''
def order_sandwiches(*types):
    for type in types: print(f'\n- A {type} sandwich has been ordered')

order_sandwiches('Pastrami with Slaw')

order_sandwiches('Roast Beef and Smoked Gouda', 'Spicy Roast Beef and Brie', 'Broccoli Rabe with Lemon Ricotta')
