# working with multiple files
'''
- Using the try-except block in this example provides 2 significant advantages. 

- We prevent our users from seeing a traceback and we let the program continue analyzing the texts it’s able to find. 

- If we don’t catch the FileNotFoundError that jane_eyre.txt raised, the user would see a full traceback and 
  the program would stop running after trying to analyze jane_eyre.txt 
  
- It would never analyze dracula.txt or baskervilles_hound.txt
'''
fileNames = ['Chapter_10/oliver_twist.txt', 
             'Chapter_10/jane_eyre.txt', 
             'Chapter_10/dracula.txt', 
             'Chapter_10/baskervilles_hound.txt', 
             'Chapter_10/frankenstein.txt']

def count_words(fileName):
    try:
        with open(fileName, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f'\n\t* {fileName} is NOT found')

        '''
        - You don’t need to report every exception you catch.
        
        - Sometimes you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened. 
        
        - To make a program fail silently, you write a try block as usual but you explicitly tell Python to do nothing in the except block. 
        
        - Python has a 'pass' statement that tells it to do nothing in a block

        - Now when a FileNotFoundError is raised, the code in the except block runs but nothing happens. 
        
        - No traceback is produced and there’s no output in response to the error that was raised

        - The 'pass' statement also acts as a placeholder. 
        
        - It’s a reminder that you’re choosing to do nothing at a specific point in your program’s execution and
          that you might want to do something there later
        '''
        pass
    else:
        word_list = contents.split()

        word_amount = len(word_list)

        print(f'\n{fileName} has about {word_amount} words')

for file in fileNames:
    count_words(file)
