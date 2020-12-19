# a series of simple if statements without any elif or else blocks
requested_toppings_0 = ['black olives', 'green peppers', 'onion', 'cheese']

if 'cheese' in requested_toppings_0:
    print('adding cheese')

if 'mushroom' in requested_toppings_0:
    print('adding mushroom')
    
if 'black olives' in requested_toppings_0:
    print('adding black olives')
    
if 'green peppers' in requested_toppings_0:
    print('adding green peppers')
    
print('\n\tfinish making your pizza')

print('\n')

# with elif & else blocks
requested_toppings_1 = ['pepperoni', 'extra cheese', 'sausage', 'bacon']

if 'extra cheese' in requested_toppings_1:
    print('adding extra cheese')
elif 'black olives' in requested_toppings_1:
    print('adding black olives')
elif 'sausage' in requested_toppings_1:
    print('adding sausage')
else:
    print('is there anything else?')

print('\n\tfinish making your pizza')