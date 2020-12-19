'''
To copy a list, you can make a slice that includes the entire original list by omitting the 1st index and the 2nd index ([:]) 

This tells Python to make a slice that starts at the 1st item & ends with the last item, producing a copy of the entire list
'''

my_foods = ['pizza', 'pasta', 'udon noodle']
friend_foods = my_foods[:]

print('my fav foods are')
print(my_foods)

print("my friend's fav foods are")
print(friend_foods)

print('\n')

# to prove these are 2 separate lists, let's add a new food to each list & then print the lists to see the updates
my_foods.append('sushi')
friend_foods.insert(1, 'hotdog')

print('my fav foods are')
print(my_foods)

print("my friend's fav foods are")
print(friend_foods)

print('\n')

''' 
try copying a list without using a slice (ex: list1 = list2)
this syntax tells python to connect list2 to list1 & vice versa 
=> now both variables point to the same list 
=> changes made in 1 list will also appear in the other 
'''
friend_foods = my_foods

friend_foods.append('lamb chop')
my_foods.insert(2, 'pork')

print('my fav foods are')
print(my_foods)

print("my friend's fav foods are")
print(friend_foods)