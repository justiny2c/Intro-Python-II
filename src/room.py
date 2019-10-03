# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, itemsList=None):
        self.name = name
        self.description = description
        self.itemsList = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def onRoomChange(self):
        print("I am in the", self.name)
        print("Where the", self.description)
        print("In here, there is a", self.itemsList)

    def addItems(self, item):
        return self.itemsList.append(item)

    def __repr__(self):
        return f'Name: {self.name}, Description: {self.description}, Items: {self.itemsList}'
