world_map = {
    'R19A': {
        'NAME': "Wiebe's Classroom",
        'DESCRIPTION': "This is the classroom that you are in right now."
                       "It has two exits to the north side",
        'PATHS': {
            'NORTH': "PARKING_LOT"

        }
    }
},
'PARKING_LOT': {
    'NAME': "The Edison Parking Lot",
    'DESCRIPTION': "There are cars parked here. To "
                   "the south is Mr. Wiebe's room",

    'PATH': {
        'SOUTH': "R19A"
    }
}