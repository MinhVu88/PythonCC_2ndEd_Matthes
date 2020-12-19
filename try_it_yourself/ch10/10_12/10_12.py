''' Favorite Number Remembered: 
- Combine dump.py & load.py from the 10_11 directory into 1 file. 
- If the number is already stored, report the favorite number to the user. 
- If not, prompt for the user’s favorite number and store it in a file. 
- Run the program twice to see that it works
'''
import json

def get_stored_num():
    fileName = 'try_it_yourself/ch10/10_12/fav_num.json'

    try:
        with open(fileName, encoding='utf-8') as f:
            fav_num = json.load(f) 
    except FileNotFoundError:
        return None
    else:
        return fav_num

def get_new_num():
    fileName = 'try_it_yourself/ch10/10_12/fav_num.json'

    fav_num = int(input('\nYour fav number: '))

    with open(fileName, 'a') as f:
        json.dump(fav_num, f)
    
    return fav_num

def get_num():
    fav_num = get_stored_num()

    if fav_num:
        print(f'\n* Your fav number: {fav_num}')
    else:
        print(f'\nThe number {get_new_num()} is now saved in fav_num.json')

get_num()
