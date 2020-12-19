prompt = "\ntell me sth & i will repeat it back to you or enter 'quit' to stop repeating: "
active = True # a flag that monitors whether or not the program should keep running

while active:
    message = input(prompt)
    if message == 'quit':
        # if the user enters 'quit', active will be set to False, 
        # meaning the condition of the while loop also becomes false
        active = False 
    else:
        print (message)