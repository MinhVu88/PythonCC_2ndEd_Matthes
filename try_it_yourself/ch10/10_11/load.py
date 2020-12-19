import json

fileName = 'try_it_yourself/ch10/10_11/fav_num.json'

try:
    with open(fileName) as f:
        fav_num = json.load(f)
    
    print(f'\n* Your fav number: {fav_num}')
except FileNotFoundError:
    print(f'\n\t{fileName} not found')
