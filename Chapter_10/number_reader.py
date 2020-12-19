# this program uses json.load() to read a list of numbers back into memory
import json

fileName = 'Chapter_10/numbers.json'

with open(fileName) as f:
    numbers = json.load(f)

print(numbers)