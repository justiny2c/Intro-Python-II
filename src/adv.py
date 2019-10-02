from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Rushi", room["outside"])
print(player)

# Write a loop that:

# * Prints the current room name
print(f"Current_Room: {player.current_room.name}")
# * Prints the current description (the textwrap module might be useful here).
print(f"Description: {player.current_room.description}")
# * Waits for user input and decides what to do.
direction = input(
    "Input n(north), e(east), s(south), w(west) to chose which direction to go...or q(quit): ")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def characterMove(direction):
    if direction == "n":
        if player.current_room.n_to is None:  # if player's current room has no room in north direction
            print("Can't go North")
        else:
            player.current_room = player.current_room.n_to
            print(player)

    elif direction == "s":
        if player.current_room.s_to is None:
            print("Can't go South")
        else:
            player.current_room = player.current_room.s_to
            print(player)

    elif direction == "e":
        if player.current_room.e_to is None:
            print("Can't go East")
        else:
            player.current_room = player.current_room.e_to
            print(player)

    elif direction == "w":
        if player.current_room.w_to is None:
            print("Can't go West")
        else:
            player.current_room = player.current_room.w_to
            print(player)
    elif direction == "q":
        print("You have exited the game")


characterMove(direction)
