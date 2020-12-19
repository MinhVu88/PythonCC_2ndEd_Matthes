''' 3-4. Guest List: 
- If you could invite anyone, living or deceased, to dinner, who would you invite? 
- Make a list that includes at least 3 people you’d like to invite to dinner. 
- Then use your list to print a message to each person, inviting them to dinner
'''
guests = ['Nikola Tesla', 'Leonardo da Vinci', 'Michael Faraday', 'Heinrich Hertz']

print(f'\nWelcome {guests[0]}, {guests[1]}, {guests[2]} & {guests[3]} to dinner!')

''' 3-5. Changing Guest List: 
- You just heard that 1 of your guests can’t make the dinner, so you need to send out a new set of invitations. 
- You’ll have to think of someone else to invite.

    + Start with your program from Exercise 3-4. 
      Add a print() call at the end of your program stating the name of the guest who can’t make it.

    + Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

    + Print a 2nd set of invitation messages, 1 for each person who is still in your list
'''
print('\n- It seems like Mr. ' + guests[2] + " can't make it tonight. So let's invite someone else")

guests[2] = 'Stephen Hawking'

print('\n- The new guest is ' + guests[2])

print(f'\nWelcome {guests[0]}, {guests[1]}, {guests[2]} & {guests[3]} to dinner!')

''' 3-6. More Guests: 
- You just found a bigger dinner table, so now more space is available. 
- Think of 3 more guests to invite to dinner.

    + Start with your program from Exercise 3-4 or Exercise 3-5. 
      Add a print() call to the end of your program informing people that you found a bigger dinner table.
    
    + Use insert() to add 1 new guest to the beginning of your list.
    
    + Use insert() to add 1 new guest to the middle of your list.
    
    + Use append() to add 1 new guest to the end of your list.
    
    + Print a new set of invitation messages, 1 for each person in your list
'''
print("\n- I've just found a bigger table, so we can invite more guests to dinner")

guests.insert(0, 'Charles Darwin')

guests.insert(3, 'Isaac Newton')

guests.append('Marie Curie')

print(f'\nWelcome {guests[0]}, {guests[1]}, {guests[2]}, {guests[3]}, {guests[4]}, {guests[5]} & {guests[6]} to dinner!')

''' 3-7. Shrinking Guest List: 
- You just found out that your new dinner table won’t arrive in time for the dinner and you have space for only 2 guests.

    + Start with your program from Exercise 3-6. 
      Add a new line that prints a message saying that you can invite only 2 people for dinner

    + Use pop() to remove guests from your list one at a time until only 2 names remain in your list. 
      Each time you pop a name from your list, print a message to that person letting them know you’re
      sorry you can’t invite them to dinner.

    + Print a message to each of the 2 people still on your list, letting them know they’re still invited.

    + Use del to remove the last 2 names from your list, so you have an empty list. 
      Print your list to make sure you actually have an empty list at the end of your program
'''
print("\n- Sorry folks, the new table won't arrive on time, so 2 seats are all i have now ")

print('\n+ Sorry ' + guests.pop(0) + ", i can't invite you to dinner")

print('\n+ Sorry ' + guests.pop(1) + ", i can't invite you to dinner")

print('\n+ Sorry ' + guests.pop(1) + ", i can't invite you to dinner")

print('\n+ Sorry ' + guests.pop(1) + ", i can't invite you to dinner")

print('\n+ Sorry ' + guests.pop(1) + ", i can't invite you to dinner")

print('\n* There are ' + str(len(guests)) + ' guests who got invited to dinner. They are ' + 
      guests[0] + ' & ' + guests[1] + '\n')

print(guests)