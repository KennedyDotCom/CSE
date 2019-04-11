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


Main_Lobby = Room("Main Lobby", "Toilets", "South Stairs", None, "Security Office", 'This is where this begins.'
                                'Your Challenge is to find a defuser and disarm a bomb. '
                                'There are Toilets on one side and stairs on another',)
Toilet = Room("Toilet", None, 'Main Lobby', None, 'Service Entrance', 'This is where you go to the bathroom.'
              'Why here you ask?' 'Ahead of you is were you make or bake food', )

Service_Entrance = Room(None, None, 'Toilet', 'Kitchen', 'This is where the service men enter at.')

Kitchen = Room(None, None, 'Service Entrance', 'Hallway', 'This is where the chef cooks his wonderful meals')

Hallway = Room('North Stairs', 'Blue Bar', 'Kitchen', 'Sunrise Bar',
               'This part connects Blue Bar, Sunrise Bar, North Stairs,and Kitchen',)

North_Stairs = Room('Hallway Up', 'Hallway Down', None, None, 'The stairs that goes up to Penthouse and Hookah Lounge',)

Hallway_Up = Room('North Stairs', 'Billiards Room', 'Vip Lounge', 'Hookah Lounge',
                  'The Hallway upstairs is the main hallway that leads to Billiards, Hookah,and Vip Lounge.',)

Billiards_Room = Room('Hallway Up', 'Aquarium', None, None, 'This is where you and your friends go to play pool.',)

Aquarium = Room('Billiards_Room', None, 'South Hallway', None, 'This is where all the fish are and swimming',)

South_Hallway = Room('Courtyard', None, 'Hallway_Up East', 'Aquarium', 'This hallway takes you to closer to the bomb.',)

Hallway_Up_East = Room('Theater', None, 'South Stairs', 'South Hallway',
                       'This is your final hallway towards the bomb.',)

Theater = Room('Penthouse', 'Hallway Up East', None, None, 'This is where you watch movies with friends or love ones',)

Penthouse = Room('Hall Of Fame', 'Theater', None, None, 'This is where you watch movies with friends or love ones',)

Hall_of_Fame = Room(None, 'Penthouse', 'Vip Lounge', None, 'This is where you go to see the best of the best.',)

Vip_Lounge = Room(None, None, 'Penthouse', None,
                  'The bomb is right there go defuse the bomb and get the hell outta there.',)

player = Player(Main_Lobby)
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

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
