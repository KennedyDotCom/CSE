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

    def move(self, new_location):
        """

        :param new_location:
        :return:
        """
        self.current_location = new_location


class Characters(object):
    def __init__(self, name, health, weapon):
            self.name = name
            self.health = health
            self.weapon = weapon

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print('%s had %d health left' % (self.name, self.health))

    def attack(self, target):
        print("%s attack %s for %d damage" % (self.name, target.name, self.take_damage()))
        target.take_damage(self.weapon.damage)


class Finka(Items):
    def __init__(self, boost):
        super(Finka, self).__init__()
        self.boost = boost
        self.health = 100
        self.time =

    def boost(self, boost):
        self.health += boost
        if self.health <= 100:
            self.boost + 25

