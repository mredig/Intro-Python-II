from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():

    items = []

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def changeRoom(self, room):
        self.current_room = room
        self.announceCurrentRoom()

    def announceCurrentRoom(self):
        output = "\n--------------\n\n"
        output += f"{self.name} is in {self.current_room.name}."
        print(output)

    def lookAroundRoom(self):
        room = self.current_room
        print(room.description)
        print("Looking around, you see the following items scattered about:")
        for item in room.items:
            print(f"\t{item.name}")

    def showInventory(self):
        print("Your are currently holding the following items in your hands:")
        for item in self.items:
            print(f"\t{item.name}")

    def pickUpItem(self, item):
        if len(self.items) >= 2:
            print("You can only hold two items at a time! (Two hands, after all) Set something down first.")
        else:
            self.current_room.removeItem(item)
            self.items.append(item)
            item.onTake(self)

    def dropItem(self, item):
        if self.holdingItem(item):
            self.items.remove(item)
            self.current_room.addItem(item)
            item.onDrop(self)

    def useItem(self, item):
        if self.holdingItem(item):
            item.onUse(self)

    def holdingItem(self, item):
        return item in self.items

    def itemNamed(self, name):
        for item in self.items:
            lcName = item.name.lower()
            if name == lcName:
                return item
