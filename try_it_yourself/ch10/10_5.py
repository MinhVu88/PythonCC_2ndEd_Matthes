''' Programming Poll: 
- Write a while loop that asks people why they like programming.
- Each time someone enters a reason, add their reason to a file that stores all the responses
'''
fileName = 'try_it_yourself/ch10/programming_poll.txt'

while True:
    reply = input("\nEnter the reason(s) you like programming or enter 'q' to quit: ")

    if reply != 'q':
        with open(fileName, 'a') as file_object:
            file_object.write(reply)

            file_object.write('\n')
    else:
        break
