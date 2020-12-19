import json

fileName = 'Chapter_10/username_0.json'

with open(fileName) as f:
    username = json.load(f)

    print(f'\nWelcome back, {username}!')