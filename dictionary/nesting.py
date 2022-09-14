#alien_0 = {
#        'color': 'green', 'points': 5}
#alien_1 = {
#        'color': 'red', 'points': 43}
#alien_2 = {
#        'color': 'brown', 'points': 23}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)
# Appending a dictionary 

high_life = []

for track_number in range(10):
    new_track = {'artist': 'ofori amponsah', 'latest': 'auntie atta', 'country': 'ghana'}
    high_life.append(new_track)

# View the first 5 tracks
# for track in high_life[:5]:
#    print(track)
#    print("......")
print(high_life)

# Modifying the dictionary
print("Modifying the dictionary items...")
for track in high_life[0:3]:
    if track['artist'] == 'oforia amponsah':
       track['latest'] = 'meweewo'
       track['county'] = 'togo'
       print(track)
