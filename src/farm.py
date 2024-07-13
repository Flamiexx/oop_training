from .field import Field
from .tractor import Tractor


class Farm:
    def __init__(self, id):
        self.id = id
        self.fields = []
        self.tractors = []

    def add_field(self, field):
        self.fields.append(field)

    def add_tractor(self, tractor):
        self.tractors.append(tractor)
