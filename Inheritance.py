class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self).__init__(name, engine_type)
        self.body_type = body_type
        self.steering_wheel = True
        self.engine_status = False  # Because the engine is off
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print('You turn the key the car turns on.')

    def move_forward(self):
        self.fuel -= 1
        print('You move forward')

    def turn_left(self):
        self.fuel -= 1
        print('You turn left.')

    def turn_right(self):
        self.fuel -= 1
        print('You turn right.')

    def turn_off(self):
        self.engine_status = False
        print('You turn the engine off.')


class Corvette(Car):
    def __init__(self):
        super(Corvette, self).__init__('Corvette', 'Gas', "slim")


julianna_car = Corvette()
julianna_car.start_engine()
julianna_car.move_forward()
