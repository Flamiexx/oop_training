class Field:
    def __init__(self, name, size, id):
        self.size = size
        self.name = name
        self.id = id
        self.tractors = []

    def add_tractor(self, tractor):

        if len(self.tractors) < 4:
            self.tractors.append(tractor)


