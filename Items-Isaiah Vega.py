class Items(object):
    def __init__(self, name):
        self.name = name


class Weapons(Items):
    def __init__(self, name, swing, block):
        super(Weapons, self).__init__(name)
        self.swing = swing
        self.block = block


class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=''):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


class Characters(object):
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon


class Player(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        self.current_location = new_location

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print('%s had %d health left' % (self.name, self.health))

    def attack(self, target):
        print("%s attack %s for %d damage" % (self.name, target.name, self.take_damage()))
        target.take_damage(self.weapon.damage)
