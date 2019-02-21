class Microwave(object):
    def __init__(self, handle=True, colors=False, plate=True, light=True):
        self.buttons = True
        self.handle = handle
        self.color = colors
        self.plate = plate
        self.light = light
        self.duration_of_time = 30

    def heat(self, time):
        if self.light:
            if self.buttons <= 0:
                print("No one hasn't started the microwave up")
            elif self.duration_of_time < time:
                print("You are done after %s", self.duration_of_time)
                self.duration_of_time = 0
            else:
                print("You are done with %s time" % time)


