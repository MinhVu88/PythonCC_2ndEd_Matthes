'''
- To write text to a file, you need to call open() with a 2nd argument 
  telling Python that you want to write to the file

- The 1st argument is still the name of the file we want to open. 

- The 2nd argument, 'w', tells Python that we want to open the file in write mode. 

- You can open a file in read mode ('r'), write mode ('w'), append mode ('a') or 
  a mode that allows you to read and write to the file ('r+') 

- If you omit the mode argument, Python opens the file in read-only mode by default.

- The open() function automatically creates the file you’re writing to if it doesn’t already exist. 

- However, be careful opening a file in write mode ('w') because if the file does exist, 
  Python will erase the contents of the file before returning the file object
'''

# writing to an empty file
fileName = 'Chapter_10/programming.txt'

with open(fileName, 'w') as file_object:
    # use the write() method on the file object to write a string to the file
    file_object.write('I love programming.\n')

    # writing multiple lines
    file_object.write('I love computers & technology.\n')

    file_object.write('I love creating & playing computer games.\n')

    file_object.write('I love hacking.\n')

# appending more info to a file
'''
- If you want to add content to a file instead of writing over existing content, you can open the file in append mode. 

- When you open a file in append mode, Python doesn’t erase the contents of the file before returning the file object.

- Any lines you write to the file will be added at the end of the file. 

- If the file doesn’t exist yet, Python will create an empty file for you
'''
with open(fileName, 'a') as file_object:
    file_object.write('I love learning about database designs.\n')

    file_object.write('I also love creating apps that can help people deal with daily issues.')
