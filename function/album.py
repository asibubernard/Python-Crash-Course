"""Album"""

def make_album(artist_name, album_title, tracks_per_album=''):
    """Album that describes a music album"""
    if tracks_per_album:
        record = {'artist': artist_name, 'album': album_title, 'tracks': 
                 tracks_per_album}
    
    else:
        record = {'artist': artist_name, 'album': album_title}
    
    return record


akwaboah = make_album('Akwaboah', 'I love you', 12)
love = make_album('westlife', 'say it all over again')
iron_boy = make_album('Amakye Dede', 'Iron Boy')


print(love)
print(iron_boy)
print(akwaboah)


"""User Albums"""

while True:
    print("\nPlease tell me the name of an artist and album...")
    print("\n(Enter 'q' to quit)")

    a_name = input("Name of Artist: ")
    
    if a_name == 'q':
        break
    
    a_title = input("Album title: ")
    if a_title == 'q':
        break
    
    album = make_album(a_name, a_title)
    print(album)
