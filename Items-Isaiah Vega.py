class Items(object):
    def __init__(self, name, use):
        self.name = name
        self.use = use


class Weapons(Items):
    def __init__(self, name, use, swing, block):
        super(Weapons, self).__init__(name, use)
        self.swing = swing
        self.block = block


class Room(object):
    def __init__(self, name):
        self.name = name


class Characters(object):
    def __init__(self, move):
        self.move = move
        self.attack = True
        self.defend = True
