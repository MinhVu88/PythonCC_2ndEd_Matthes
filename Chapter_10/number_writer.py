'''
- Many of your programs will ask users to input certain kinds of info.

- You might allow users to store preferences in a game or provide data for a visualization. 

- Whatever the focus of your program is, you’ll store the info users provide in data structures such as lists and dictionaries.

- When users close a program, you’ll almost always want to save the info they entered. 

- A simple way to do this involves storing your data using the json module.

- The json module allows you to dump simple Python data structures into a file and 
  load the data from that file the next time the program runs. 

- You can also use json to share data between different Python programs. 

- Even better, the JSON data format is not specific to Python, 
  so you can share data you store in the JSON format with people who work in many other programming languages
'''
#  this program uses the json.dump() function to store a set of numbers
import json

numbers = [47, 23, 51, 7, 69]

# it’s customary to use .json to indicate that the data in the file is stored in the JSON format
fileName = 'Chapter_10/numbers.json'

with open(fileName, 'w') as f:
    # The function takes 2 arguments: a piece of data to store & a file object it can use to store the data
    json.dump(numbers, f)