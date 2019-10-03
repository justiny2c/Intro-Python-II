from room import Room
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    "weapon": Items("Lightsaber", "Luke Skywalker's saber"),
    "armour": Items("Shield", "Captain America's shield"),
    "phone": Items("iPhone", "Necessary for emergency calls"),
    "shoes": Items("Vapormax's", "Nike Swoosh all day for running")
}

# add items to each room

room['foyer'].addItems('weapon') 
room['outside'].addItems('shield')
room['overlook'].addItems('phone')
room['narrow'].addItems('shoes')
room['treasure'].addItems('weapon')

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Main

# Make a new player object that is currently in the 'outside' room.

player = Player("Rushi", room["outside"])
# print(player)

# Write a loop that:

print(f"{player.name} is in Current_Room: {player.current_room.name}")
print(f"Description: {player.current_room.description}")
print(f"Items: {player.current_room.itemsList}")

# * Waits for user input and decides what to do.
while True:
    itemDrop = input(
        "Do you want to drop an item from your inventory? No(0), First(1), Second(2), Third(3)...etc: ")
    player.drop(int(itemDrop)-1)
    item = input(
        "Do you want to take an item? No(0), First(1) or Second(2)...: ")
    player.take(int(item)-1)
    direction = input(
        "Input n(north), e(east), s(south), w(west) to chose which direction to go...or q(quit): ")
    player.move(direction)


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# def characterMove(direction):
#     if direction == "n":
#         if player.current_room.n_to is None:  # if player's current room has no room in north direction
#             print("Can't go North")
#         else:
#             player.current_room = player.current_room.n_to
#             print(player)

#     elif direction == "s":
#         if player.current_room.s_to is None:
#             print("Can't go South")
#         else:
#             player.current_room = player.current_room.s_to
#             print(player)

#     elif direction == "e":
#         if player.current_room.e_to is None:
#             print("Can't go East")
#         else:
#             player.current_room = player.current_room.e_to
#             print(player)

#     elif direction == "w":
#         if player.current_room.w_to is None:
#             print("Can't go West")
#         else:
#             player.current_room = player.current_room.w_to
#             print(player)
#     elif direction == "q":
#         print("You have exited the game")


# characterMove(direction)
