coastline = {
    'Main Lobby': {
        'NAME': 'Main Lobby',
        'DESCRIPTION': 'This is where this begins. \n '
                       'Your Challenge is to find a defuser and disarm a bomb. \n '
                       'There are Toilets on one side and stairs on another',
        'PATHS': {
            'NORTH':  'TOILETS',
            'SOUTH':  'SOUTH STAIRS',
            'EAST':   'CANT GO THAT WAY!!',
            'WEST':   'SECURITY OFFICE'
        }
    },
    'TOILETS': {
        'NAME': 'TOILETS',
        'DESCRIPTION': 'This is where you go to the bathroom. \n'
                       'Why here you ask?\n'
                       'Ahead of you is were you make or bake food',
        'PATHS': {
            'NORTH': 'WALL',
            'SOUTH': 'MAIN LOBBY',
            'EAST':  'WALL',
            'WEST':  'SERVICE ENTRANCE'
        }
    },
    'SERVICE ENTRANCE': {
        'NAME': 'SERVICE ENTRANCE',
        'DESCRIPTION': 'This is where the service men enter at.',
    
        'PATHS': {
            'NORTH': 'WALL',
            'SOUTH': 'WALL',
            'EAST': 'TOILETS',
            'WEST': 'KITCHEN'
        }
    },
    'KITCHEN': {
        'NAME': 'KITCHEN',
        'DESCRIPTION': 'This is where the chef cooks his wonderful meals',

        'PATHS': {
            'NORTH': 'WALL',
            'SOUTH': 'WALL',
            'EAST': 'SERVICE ENTRANCE',
            'WEST': 'HALLWAY'
        }
    },
    'HALLWAY': {
        'NAME': 'HALLWAY',
        'DESCRIPTION': 'This part connects Blue Bar, Sunrise Bar, North Stairs,and Kitchen',

        'PATHS': {
            'NORTH': 'NORTH STAIRS',
            'SOUTH': 'BLUE BAR',
            'WEST': 'SUNRISE BAR',
            'EAST': 'KITCHEN'
        }
    },
    'NORTH STAIRS': {
        'NAME': 'NORTH STAIRS',
        'DESCRIPTION': 'The stairs that goes up to Penthouse and Hookah Lounge',

        'PATHS': {
            'NORTH': 'HALLWAY UP',
            'SOUTH': 'HALLWAY DOWN',
            'EAST': 'WALL',
            'WEST': 'WALL'
        }
    },
    'HALLWAY UP': {
        'NAME': 'HALLWAY UP',
        'DESCRIPTION': 'The Hallway upstairs is the main hallway that leads to Billiards, Hookah,and Vip Lounge.',

        'PATHS': {
            'NORTH': 'NORTH STAIRS',
            'SOUTH': 'BILLIARDS ROOM',
            'EAST':  'VIP LOUNGE',
            'WEST':  'HOOKAH LOUNGE'
        }
    },
    'BILLIARDS ROOM': {
        'NAME': 'BILLIARDS ROOM',
        'DESCRIPTION': 'This is where you and your friends go to play pool.',

        'PATHS': {
            'NORTH': 'HALLWAY UP',
            'SOUTH': 'AQUARIUM',
            'EAST': 'WALL',
            'WEST': 'WALL'
        }
    },
    'AQUARIUM': {
        'NAME': 'AQUARIUM',
        'DESCRIPTION': 'This is where all the fish are and swimming',

        'PATHS': {
            'NORTH': 'BILLARDS ROOM',
            'SOUTH': 'WALL',
            'EAST': 'SOUTH HALLWAY',
            'WEST': 'WALL'
        }
    },
    'SOUTH HALLWAY': {
        'NAME': 'SOUTH HALLWAY',
        'DESCRIPTION': 'This hallway takes you to closer to the bomb.',

        'PATHS': {
            'NORTH': 'COURTYARD',
            'SOUTH': 'WALL',
            'EAST': 'HALLWAY UP EAST',
            'WEST': 'AQUARIUM'
        }
    },
    'HALLWAY UP EAST': {
        'NAME': 'HALLWAY EAST',
        'DESCRIPTION': 'This is your final hallway towards the bomb.',

        'PATHS': {
            'NORTH': 'THEATER',
            'SOUTH': 'WALL',
            'EAST': 'SOUTH STAIRS',
            'WEST': 'SOUTH HALLWAY'
        }
    },
    'THEATER': {
        'NAME': 'THEATER',
        'DESCRIPTION': 'This is where you watch movies with friends or love ones',

        'PATHS': {
            'NORTH': 'PENTHOUSE',
            'SOUTH': 'HALLWAY UP EAST',
            'EAST': 'WALL',
            'WEST': 'WALL'
        }
    },
    'PENTHOUSE': {
        'NAME': 'PENTHOUSE',
        'DESCRIPTION': 'This is where you stay a sleep in the nice air of Spain',

        'PATHS': {
            'NORTH': 'HALL OF FAME',
            'SOUTH': 'THEATER',
            'EAST': 'WALL',
            'WEST': 'WALL'
        }
    },
    'HALL OF FAME': {
        'NAME': 'HALL OF FAME',
        'DESCRIPTION': 'This is where you go to see the best of the best.',

        'PATHS': {
            'NORTH': 'WALL',
            'SOUTH': 'PENTHOUSE',
            'EAST': 'VIP LOUNGE',
            'WEST': 'WALL'
        }

    },
    'VIP LOUNGE': {
        'NAME': 'VIP LOUNGE',
        'DESCRIPTION': 'The bomb is right there go defuse the bomb and get the hell outta there.',

        'PATHS': {
            'NORTH': 'WALL',
            'SOUTH': 'WALL',
            'EAST': 'PENTHOUSE',
            'WEST': 'WALL'
        }

    }
}


current_node = coastline['Main Lobby']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
playing = True

while playing:
    print(current_node('NAME'))
    command = input('>_')
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = coastline[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print('Command not recognized')
