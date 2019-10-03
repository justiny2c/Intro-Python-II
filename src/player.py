# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __repr__(self):
        return f'Name: {self.name}, Current_Room: {self.current_room}'

    def move(self, direction):
        moveList = ["n", "e", "s", "w"]
        try:
            moveList.index(direction)
            if(direction == "q"):
                return
            
            thisRoom = getattr(self.current_room, direction + "_to")

            if(thisRoom):
                self.current_room = thisRoom
            else:
                print("Space does not exist")
            self.current_room.onRoomChange()
        except:
            print("Failed")
            pass
