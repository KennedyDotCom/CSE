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
        },
    'SERVICE ENTRANCE': {
        'NAME': 'SERVICE ENTRANCE',
        'DESCRIPTION': 'This is where the service men enter at.',
    
        'PATHS': {
            'NORTH': 'WALL',
            'SOUTH': 'WALL',
            'EAST': 'TOILETS',
            'WEST': 'KITCHEN'
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
        'DESCRIPTION':'This part connects Blue Bar, Sunrise Bar, North Stairs,and Kitchen',

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
    '': '',


    }

}
