class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description


R19A = Room("R19A")
parking_lot = Room('The parking lot', None, R19A)

R19A.north = parking_lot


R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The parking lot', None, R19A)