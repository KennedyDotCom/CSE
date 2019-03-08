class Items(object):
    def __init__(self, name, use):
        self.name = name
        self.use = use


class Weapons(Items):
    def __init__(self, name, use, swing):
        super(Weapons, self).__init__(name, use)
        self.swing =  swing
        self.
