class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=''):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


class Items(object):
    def __init__(self, name):
        self.name = name


class Weapons(Items):
    def __init__(self, name, damage):
        super(Weapons, self).__init__(name)
        self.damage = damage


class SledgeHammer(Weapons):
    def __init__(self):
        super(SledgeHammer, self).__init__()
        self.swing = True


class Stim(Items):
    def __init__(self, name, heal):
        super(Stim, self).__init__(name)
        self.heal = heal


class Rook(Items):
    def __init__(self):
        super(Rook, self).__init__(Rook)
        self.armor = 25


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.armor = 0
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def heal(self, health):
        if health > 100:
            health += 25

    def plates(self, armor):
        if armor > 0:
            armor += 25


Coastline = Room("Coastline")
Main_Lobby = Room("Toliet", 'South Stairs')