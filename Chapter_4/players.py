players = ['maynard', 'paul', 'adam', 'danny', 'justin', 'billy']

print(players[0:3])

print(players[1:4])

print(players[:5])

print(players[3:])

print(players[-2:])

print('\n')

# use a slice in a for loop
print('The 1st 4 players:')

for player in players[0:4]:
    print('- ' + player.title())