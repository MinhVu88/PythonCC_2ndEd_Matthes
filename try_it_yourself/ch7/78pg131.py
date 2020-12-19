sandwich_orders = ['cheese', 'tuna fish', 'submarine', 'ham', 'chicken', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    sandwich_in_progress = sandwich_orders.pop()
    print ('\n- i made your ' + sandwich_in_progress + ' sandwich')
    finished_sandwiches.append(sandwich_in_progress)

print ('\nThe following sandwiches have been made:')
for sandwich in finished_sandwiches:
    print ('\n+ ' + sandwich + ' sandwiches')