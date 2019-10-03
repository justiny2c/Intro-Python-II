# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __repr__(self):
        return f'Name: {self.name}, Current_Room: {self.current_room}'

    def take(self, item):
        # itemsInRoom = ["weapon", "shield", "phone", "shoes"]
        # try:
        #     itemsInRoom.index(item)
        if item == -1:
            print("You didn't grab anything")
            return
        else:
            self.inventory.append(self.current_room.itemsList[item])
            print("You grabbed an item")

    def drop(self, itemDrop):
        if itemDrop == -1:
            print("You didn't drop anything")
            return
        else:
            self.inventory.remove(self.inventory[itemDrop])
            print("You dropped an item")

    def move(self, direction):
        moveList = ["n", "e", "s", "w", "q"]
        try:
            moveList.index(direction)
            if(direction == "q"):
                return

            thisRoom = getattr(self.current_room, direction + "_to")

            if(thisRoom):
                self.current_room = thisRoom
            else:
                print("CAN'T GO ANY FURTHER")
            print("\n \n")
            self.current_room.onRoomChange()

        except:
            print("Failed")
            pass
