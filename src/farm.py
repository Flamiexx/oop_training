from .field import Field
from .tractor import Tractor


class Farm:
    def __init__(self, id):
        self.__id = id
        self.__fields = []
        self.__tractors = []

    def add_field(self, field):
        self.__fields.append(field)

    def add_tractor(self, tractor):
        self.__tractors.append(tractor)
