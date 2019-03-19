class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.shield = 100
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print('%s had %d health left' % (self.name, self.health))

    def attack(self, target):
        print("%s attack %s for %d damage" % (self.name, target.name, self.take_damage()))
        target.take_damage(self.weapon.damage)


R19A = Room("R19A")
parking_lot = Room('The parking lot', None, R19A)

# Items
sword = Weapon("Sword", 15)
sword2 = Weapon("Orc Sword", 5)

print(Player)
# Player
Player = R19A
print()

R19A.north = parking_lot

R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The parking lot', None, R19A)

playing = True
directions = ['north', 'south', 'east', 'west']

while playing:
    print(Player.current_location.name)
    print(Player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            # command = 'north'
            room_name = getattr(Player.current_location, command)
            room_object = globals()[room_name]

            Player.move(room_object)
        except KeyError:
            print("This key does not exist.")
        except AttributeError:
            print("I can't go that way")
    else:
        print("Command Not Recognized")
