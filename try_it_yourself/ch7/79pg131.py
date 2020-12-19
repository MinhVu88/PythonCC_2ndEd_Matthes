sandwich_orders = ['cheese', 'pastrami', 'tuna fish', 'submarine', 'pastrami', 'ham', 'chicken', 'grilled cheese', 'pastrami']
print (sandwich_orders)
print ('\nthe deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print ('\n')
print (sandwich_orders)