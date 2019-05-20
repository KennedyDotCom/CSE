class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description='', items=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.items = items


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
    def __init__(self,name, boost):
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


defuser_a = Defuser("defuser", True)
Drone_a = Drone('Drone', 5)
Stim_a = Stim('Stim', 25)
Rook_a = Rook('Rook', 25)
SledgeHammer_a = SledgeHammer('SledgeHammar', 100)
Claymore_a = Claymore("Claymore", 100)
Canster_a = Canster('Canster', 10)
Frag_a = Frag('Frag', 99)
Finka_a = Finka('Finka', 20)
FlashBang_a = FlashBang("FlashBang", 10)
Gu_a = Gu("Gu", 15)
ShockDrone_a = ShockDrone('ShockDrone', 10)
Shield_a = Shield("Shield", 100)
KapKan_a = KapKan("KapKan", 60)
BearTrap_a = BearTrap('BearTrap', 100)


Main_Lobby = Room("Main_Lobby", "Toilet", "South_Stairs", "Security_Office", 'Courtyard', 'This is where this begins.'
                                'Your Challenge is to get the defuser and disarm a bomb. Also if you look on the floor.'
                                'there is a defuser and a drone get it and '
                                'explore the map')

Toilet = Room("Toilet", None, 'Main_Lobby', None, 'Service_Entrance', 'This is where you go to the bathroom.'
              'Why here you ask?' 'Ahead of you is were you make or bake food')

Service_Entrance = Room('Service_Entrance', None, None, 'Toilet', 'Kitchen', 'This is where the service men enter at.')

Kitchen = Room('Kitchen', None, None, 'Service_Entrance', 'Hallway',
               'This is where the chef cooks his wonderful meals')

Hallway = Room('Hallway', 'North_Stairs', 'Blue_Bar', 'Kitchen', 'Sunrise_Bar',
               'This part connects Blue_Bar, Sunrise_Bar, North_Stairs,and Kitchen')

North_Stairs = Room('North_Stairs', 'Hallway_Up', 'Hallway_Down', None, None,
                    'The stairs that goes up to Penthouse and Hookah Lounge')

Hallway_Up = Room('Hallway_Up', 'North_Stairs', 'Billiards_Room', 'Vip_Lounge', 'Hookah_Lounge',
                  'The Hallway upstairs is the main hallway that leads to Billiards, Hookah,and Vip Lounge.')

Billiards_Room = Room('Billiards_Room', 'Hallway_Up', 'Aquarium', None, None,
                      'This is where you and your friends go to play pool.')

Aquarium = Room('Aquarium', 'Billiards_Room', None, 'South_Hallway', None,
                'This is where all the fish are and swimming')

South_Hallway = Room('South_Hallway', 'Courtyard', None, 'Hallway_Up_East', 'Aquarium',
                     'This hallway takes you to closer to the bomb.')

South_Stairs = Room('South_Stairs', 'Main_Lobby', None, 'Hallway', None, 'The Stairs that leads up stairs.')

Hallway_Up_East = Room('Hallway_Up_East', 'Theater', None, 'South_Stairs', 'South_Hallway',
                       'This is your final hallway towards the bomb.')

Theater = Room('Theater', 'Penthouse', 'Hallway_Up_East', None, None,
               'This is where you watch movies with friends or love ones')

Penthouse = Room('Penthouse', 'Hall_Of_Fame', 'Theater', None, None,
                 'This is where you watch movies with friends or love ones')

Hall_of_Fame = Room('Hall_of_Fame', None, 'Penthouse', 'Vip_Lounge', None,
                    'This is where you go to see the best of the best.')

Vip_Lounge = Room('Vip_Lounge', None, None, 'Penthouse', None,
                  'The bomb is right there go defuse the bomb and get the hell outta there.')

Main_Lobby.items = [defuser_a, Drone_a]
Toilet.items = [SledgeHammer_a]
Service_Entrance.items = [ShockDrone_a, Stim_a]
Kitchen.items = [Rook_a]

win_condition = False
player = Player(Main_Lobby)
playing = True
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']


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
    elif 'defuse bomb' in command.lower() and player.current_location == Vip_Lounge:
        print("You try to defuse the bomb, there are 5 wires which do you want to cut")
        print("Which one do you choose to cut?")
        print("| | | | |\n| | | | |\n| | | | |")
        bomb_com = input(">_")
        if bomb_com.lower() in ["1", "first"]:
            print("You cut the first wire, and the bomb exploded")
            playing = False
        elif bomb_com.lower() in ["2", "second"]:
            print("You defused the bomb!")
            win_condition = True
        elif bomb_com.lower() in ["3", "third"]:
            print("You cut the third wire, and the bomb exploded")
            playing = False
        elif bomb_com.lower() in ["4", "forth"]:
            print("You cut the forth wire, and the bomb exploded")
            playing = False
        elif bomb_com.lower() in ["5", "fifth"]:
            print("You cut the fifth wire, and the bomb exploded")
            playing = False

    elif 'attack' in command:
        target_item = command[7:]

    elif 'get' in command:
        target_items = command[4:]
        found_items = None
        for thing in player.current_location.items:
            if thing.name == target_items:
                found_items = thing
            if found_items is not None:
                print("You picked up %s" % found_items.name)
                player.inventory.append(found_items)
                for i, items in enumerate(player.current_location.items):
                    if items.name == found_items.name:
                        player.current_location.items.pop(i)
            else:
                print("That doesn't exist")
        else:
            print('Command Not Recognized')

if not playing and not win_condition:
    print("GAME OVER")
else:
    print("You Saved the World")

