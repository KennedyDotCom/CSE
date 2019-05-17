class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=''):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.items = []


class Items(object):
    def __init__(self, name):
        self.name = name


class Weapons(Items):
    def __init__(self, name, damage):
        super(Weapons, self).__init__(name)
        self.durability = 100
        self.damage = damage


class Heal(Items):
    def __init__(self, name, heal):
        super(Heal, self).__init__(name)
        self.heal = heal


class Wire(Weapons):
    def __init__(self, name, damage):
        super(Wire, self).__init__(name, damage)
        self.damage = 5


class Frag(Weapons):
    def __init__(self, name, damage):
        super(Frag, self).__init__(name, damage)
        self.damage = 20


class BearTrap(Weapons):
    def __init__(self, name, damage):
        super(BearTrap, self).__init__(name, damage)
        self.damage = 100


class Canster(Weapons):
    def __init__(self, name, damage):
        super(Canster, self).__init__(name, damage)
        self.damage = 5


class KapKan(Weapons):
    def __init__(self, name, damage):
        super(KapKan, self).__init__(name, damage)
        self.damage = 60


class Gu(Weapons):
    def __init__(self, name, damage):
        super(Gu, self).__init__(name, damage)
        self.damage = 4


class ShockDrone(Weapons):
    def __init__(self, name, damage):
        super(ShockDrone, self).__init__(name, damage)
        self.damage = 5


class Shield(Weapons):
    def __init__(self, name, damage):
        super(Shield, self).__init__(name, damage)
        self.damage = 10


class FlashBang(Weapons):
    def __init__(self, name, dizzy):
        super(FlashBang, self).__init__(name, dizzy)
        self.dizzy = dizzy


class Finka(Heal):
    def __init__(self, name, boost):
        super(Finka, self).__init__(name, boost)
        self.boost = 25


class Claymore(Weapons):
    def __init__(self, name, damage):
        super(Claymore, self).__init__(name, damage)
        self.damage = damage


class Drone(Weapons):
    def __init__(self, name, damage):
        super(Drone, self).__init__(name, damage)
        self.name = name
        self.damage = 5
        self.durability = 100


class SledgeHammer(Weapons):
    def __init__(self, damage, name):
        super(SledgeHammer, self).__init__(damage, name)
        self.swing = True


class Stim(Heal):
    def __init__(self, name, heal):
        super(Stim, self).__init__(name, heal)
        self.heal = heal


class Rook(Heal):
    def __init__(self, name, armor):
        super(Rook, self).__init__(name, armor)
        self.armor = 25


class Defuser(Items):
    def __init__(self, name, usable=True):
        super(Defuser, self).__init__(name)
        self.usable = usable


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.armor = 0
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """

        :param new_location:
        :return:
        """

        self.current_location = new_location

    def heal(self, health):
        if health > 100:
            health += 25

    def plates(self, armor):
        if armor < 0:
            armor += 25


class Characters(object):
    def __init__(self, name, health, armor, weapon):
            self.name = name
            self.health = health
            self.armor = armor
            self.weapon = weapon

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print('%s had %d health left' % (self.name, self.health))

    def attack(self, target):
        print("%s attack %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)
`

