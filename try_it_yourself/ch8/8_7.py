''' Album: 
- Write a function called make_album() that builds a dictionary describing a music album. 

- The function should take in an artist name and an album title 
  and it should return a dictionary containing these 2 pieces of information. 

- Use the function to make 3 dictionaries representing different albums. 

- Print each return value to show that the dictionaries are storing the album information correctly.

- Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 

- If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 

- Make at least 1 new function call that includes the number of songs on an album
'''
def make_album(artist, album, songs=None):
    album_dic = {'ar': artist, 'al': album}

    if songs: album_dic['songs'] = songs

    return album_dic

print(make_album('Tool', 'Opiate'))

print(make_album('Tool', 'Undertow'))

print(make_album('Tool', 'Aenima'))

print(make_album('Tool', 'Lateralus', songs=13))
