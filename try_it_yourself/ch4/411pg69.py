my_pizzas = ['pepperoni', 'mushroom', 'cheese', 'bacon', 'sausage']
friend_pizzas = my_pizzas[:]

my_pizzas.append('onion')
friend_pizzas.insert(1, 'black olives')

print('My fav pizzas:')
for pizza in my_pizzas:
    print('\n\t' + str(pizza))

print("\nMy friend's fav pizzas:")
for pizza in friend_pizzas:
    print('\n\t' + str(pizza))