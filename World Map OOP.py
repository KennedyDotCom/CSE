class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.shield = 100
        self.inventory = []
        self.damage = 10

    def move(self, newlocation):
        """This method moves a character to a new location

        :param newlocation: The variable containing a room object
        """
        self.current_location = newlocation


R19A = Room("R19A")
parking_lot = Room('The parking lot', None, R19A)


R19A.north = parking_lot

R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The parking lot', None, R19A)

player = Player(R19A)
playing = True
directions = ['north', 'south', 'east', 'west']

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
            print("This key does not exist.")
        except AttributeError:
            print("I can't go that way")
    else:
        print("Command Not Recognized")
