''' Lottery: 
- Make a list or tuple containing a series of 10 numbers and 5 letters.
- Randomly select 4 numbers or letters from the list and print a message saying that 
  any ticket matching these 4 numbers or letters wins a prize
'''
from random import choice, randint

numbers = []

count1 = 1

while count1 <= 10:
    numbers.append(randint(0, 10))
    count1 += 1

print(numbers)

# 97 - 122 == a - z
letters = []

count2 = 1

while count2 <= 5:
    letters.append(chr(randint(97, 122)))
    count2 += 1

print(letters)

numbers += letters

tickets_tuple = tuple(numbers)

print(tickets_tuple)

winning_list = []

while len(winning_list) < 4:
    chosen_ticket = choice(tickets_tuple)

    if chosen_ticket not in winning_list:
        winning_list.append(chosen_ticket)
        
for ticket in winning_list:
    print(f'\nThe winning ticket: {ticket}')
