""" Slicing a list """
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:3])
# print(players[1:4])
# print(players[0:])
# print(players[2:1])

""" Lopping through a slice"""

for player in players[:3]:
    print(player.title())

