# saving & reading user-generated data
import json

username = input('\nUsername: ')

fileName = 'Chapter_10/username_0.json'

with open(fileName, 'w') as f:
    json.dump(username, f)

    print(f"\nYour username '{username}' has been remembered")