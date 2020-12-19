# handling the FileNotFoundError exception
fileName = 'Chapter_10/alice.txt'

try:
    '''
    - There are 2 changes here: 
    
    - The 1st change is the use of the variable f to represent the file object, which is a common convention. 
    
    - The 2nd is the use of the encoding argument, which is needed when your system’s default encoding 
      doesn’t match the encoding of the file that’s being read 
    '''
    with open(fileName, encoding='utf-8') as f:
        contents = f.read() # let's try to read a file that doesn’t exist
except FileNotFoundError:
    print(f'\n\t* {fileName} is not found')
else:
    # This code is placed in the else block as it will work only if the code in the try block was executed successfully
    # The split() method separates a string into parts wherever it finds a space & stores all the parts of the string in a list
    word_list = contents.split()

    word_amount = len(word_list)

    print(f'\n{fileName} has about {word_amount} words')
