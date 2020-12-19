# a different version of 74pg127
toppings_requests = ''
active = True

while active:
    toppings_requests = input('\nplz enter your fav pizza toppings: ')
    if toppings_requests == 'quit':
        break
    else:
        print ("\ti'll add " + toppings_requests + ' to your pizza toppings')