''' Guest Book: 
- Write a while loop that prompts users for their name. 
- When they enter their name, print a greeting to the screen and 
  add a line recording their visit in a file called guest_book.txt. 
- Make sure each entry appears on a new line in the file
'''
fileName = 'try_it_yourself/ch10/guest_book.txt'

while True:
    reply = input("\nEnter your name or enter 'q' to quit: ")

    if reply != 'q':
        print(f'\n- Hello {reply.title()}')

        with open(fileName, 'a') as file_object:
            file_object.write(reply.title())

            file_object.write('\n')
    else:
        break

