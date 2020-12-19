'''
- Let’s start by looking at the open() function. 

- To do any work with a file, even just printing its contents, you 1st need to open the file to access it. 

- The open() function needs 1 argument: the name of the file you want to open. 

- Python looks for this file in the directory where the program that’s currently being executed is stored

- The keyword 'with' closes the file once access to it is no longer needed.

- Notice how we call open() in this program but not close(). 

- You could open and close the file by calling open() and close() 
  but if a bug in your program prevents the close() method from being executed, the file may never close.

- This may seem trivial but improperly closed files can cause data to be lost or corrupted. 

- And if you call close() too early in your program, you’ll find yourself trying to work with a closed file 
  (a file you can’t access), which leads to more errors
'''

# reading an entire file
'''
- In this example, file_reader.py is currently running, 
  so Python looks for pi_digits.txt in the directory where file_reader.py is stored. 

- The open() function returns an object representing the file. 

- Here, open('pi_digits.txt') returns an object representing pi_digits.txt. 

- Python assigns this object to file_object, which we’ll work with later in the program
'''
with open('Chapter_10/pi_digits.txt') as file_object1:
    '''
    - Once we have a file object representing pi_digits.txt, we use the read() method to read the entire contents 
      of the file and store it as 1 long string in contents. 
    
    - When we print the value of contents, we get the entire text file back
    '''
    contents1 = file_object1.read()

'''
- The only difference between this output and the original file is the extra blank line at the end of the output. 

- The blank line appears because read() returns an empty string when it reaches the end of the file; 
  this empty string shows up as a blank line
'''
print(len(contents1))

print(contents1)

print('------------------')

with open('Chapter_10/pi_digits.txt') as file_object2:
    contents2 = file_object2.read()
    
    print(len(contents2))
    
    print(contents2.rstrip()) # use rstrip() in the call to print() to remove the extra blank line

print('------------------')

# reading line by line
abs_path = 'Chapter_10/pi_digits.txt' # it's a common convention to assign the filename we're reading from to a var

with open(abs_path) as file_object3:
    # use a for loop on the file object to examine each line from the file 1 at a time
    for line in file_object3:
        print(f'* {line.rstrip()}')

print('------------------')

# making a list of lines from a file
with open(abs_path) as file_object4:
    lines = file_object4.readlines() # the readlines() method takes each line from the file and stores it in a list

for line in lines:
    print(f'- {line.rstrip()}')

