#prompt = '\nplz enter your fav pizza toppings: '
toppings_requests = ''

while toppings_requests != 'quit':
    #toppings_requests = input(prompt)
    toppings_requests = input('\nplz enter your fav pizza toppings: ')
    if toppings_requests != 'quit':
        print ("\ti'll add " + toppings_requests + ' to your pizza toppings')
    else:
        print ('\tthanks for visiting our restaurant')