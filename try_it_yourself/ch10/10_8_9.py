''' 
* 10_8.py (Cats and Dogs): 

- Make 2 files, cats.txt and dogs.txt. 
- Store at least 3 names of cats in the 1st file and 3 names of dogs in the 2nd file. 
- Write a program that tries to read these files and print the contents of the file to the screen. 
- Wrap your code in a try-except block to catch the FileNotFound error and print a friendly message if a file is missing. 
- Move 1 of the files to a different location on your system and make sure the code in the except block executes properly.

* 10_9.py (Silent Cats and Dogs): Modify your except block in Exercise 10-8 to fail silently if either file is missing
'''
file1 = 'try_it_yourself/ch10/cats.txt'

file2 = 'try_it_yourself/ch10/dogs.txt'

file3 = 'try_it_yourself/ch10/fairies.txt'

files = [file1, file2, file3]

def get_pets(fileName):
    try:
        with open(fileName, encoding='utf-8') as f:
            contents = f.read()

            print(contents)
    except FileNotFoundError:
        #print(f'\n* {fileName} -> not found')

        pass
    

for file in files:
    get_pets(file)

