prompt = "\ntell me sth & i will repeat it back to you or enter 'quit' to stop repeating: "
message = ''

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print (message)