''' User Albums: 
- Start with 8_7.py, write a while loop that allows users to enter an album’s artist and title. 
- Once you have that info, call make_album() with the user’s input and print the dictionary that’s created. 
- Be sure to include a quit value in the while loop
'''
def make_album(artist, album, songs=None):
    album_dic = {'ar': artist, 'al': album}

    if songs: album_dic['songs'] = songs

    return album_dic

while True:
    art = input("\nYour fav artist or enter 'q' to quit: ")

    if art == 'q': break

    alb = input("\nYour fav album of his/hers/theirs or enter 'q' to quit: ")

    if alb == 'q': break

    print('\n')

    print(make_album(art, alb))
