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
        self.damage = damage


class SledgeHammer(Weapons):
    def __init__(self, damage, name):
        super(SledgeHammer, self).__init__(damage, name)
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

    def move(self, new_location):
    self.current_location = new_location




    def heal(self, health):
        if health > 100:
            health += 25

    def plates(self, armor):
        if armor > 0:
            armor += 25


Main_Lobby = Room("Main Lobby", "Toilets", "South Stairs", None, "Security Office", 'This is where this begins.'
                                'Your Challenge is to find a defuser and disarm a bomb. '
                                'There are Toilets on one side and stairs on another',)
Toilet = Room("Toilet", None, 'Main Lobby', None, 'Service Entrance',)

player = Player(Main_Lobby)
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            # command = 'north'
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("This key does not exist")
        except AttributeError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")