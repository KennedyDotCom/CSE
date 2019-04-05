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


class SledgeHammer(Weapons):
    def __init__(self, damage, name):
        super(SledgeHammer, self).__init__(damage, name)
        self.swing = True


class Stim(Items):
    def __init__(self, name, heal):
        super(Stim, self).__init__(name)
        self.heal = heal


class Rook(Items):
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


defuser = Defuser("Defuser", True)

Stim = Stim("Stim Pistol", 25)

Rook = Rook("Rook Armor", 50)

Main_Lobby = Room("Main Lobby", "Toilets", "South Stairs", None, "Security Office", 'This is where this begins.'
                                'Your Challenge is to find a defuser and disarm a bomb. '
                                'There are Toilets on one side and stairs on another', defuser)
Toilet = Room("Toilet", None, 'Main Lobby', None, 'Service Entrance', 'This is where you go to the bathroom.'
              'Why here you ask?' 'Ahead of you is were you make or bake food', )

Service_Entrance = Room(None, None, 'Toilet', 'Kitchen', 'This is where the service men enter at.')

Kitchen = Room(None, None, 'Service Entrance', 'Hallway','This is where the chef cooks his wonderful meals')

Hallway = Room('North Stairs', 'Blue Bar', 'Kitchen', 'Sunrise Bar',
               'This part connects Blue Bar, Sunrise Bar, North Stairs,and Kitchen',)



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