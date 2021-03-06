class Item():
    def __init__(self, name):
        self.name = name

    def onTake(self, player):
        print(f"{player.name} picked up {self.name}.")

    def onDrop(self, player):
        print(f"{player.name} is no longer holding {self.name}.")

    def onUse(self, player):
        print(f"Using {self.name}...")

    

class Rock(Item):
    def __init__(self, name):
        super().__init__(name)
        self.isThrown = False

    def onTake(self, player):
        self.isThrown = False
        super().onTake(player)

    def onUse(self, player):
        print(f"Threw {self.name}")
        self.isThrown = True
        player.dropItem(self.name.lower())

    def onDrop(self, player):
        if not self.isThrown:
            super().onDrop(player)

class Chair(Item):
    def __init__(self, name):
        super().__init__(name)
        self.isBroken = False

    def onUse(self, player):
        if self.isBroken:
            print("The chair is broken. If you sit on it, you could severely injure yourself.")
        else:
            print("""You sit on the chair for a moment, relaxing. \
This long journey is taxing, so it's nice take a small re...
...
...
The chair broke. You're too fat.
""")
            self.name = f"Broken{self.name}"
            self.isBroken = True

class FlavorItem(Item):
    def __init__(self, name, flavorText):
        super().__init__(name)
        self.flavorText = flavorText

    def onUse(self, player):
        print(self.flavorText)

class Box(Item):
    def __init__(self, name, content):
        super().__init__(name)
        self.content = None
        if type(content) == Item:
            self.content = content

    def onUse(self, player):
        if self.content:
            print(f"You open {self.name} and {self.content.name} falls out onto the ground!")
            room = player.current_room
            room.addItem(self.content)
            self.content = None
        else:
            print(f"{self.name} is empty!")
