class Field:
    def __init__(self, name, size, id):
        self.__size = size
        self.__name = name
        self.__id = id
        self.__tractors = []

    def add_tractor(self, tractor):

        if len(self.__tractors) < 4:
            self.__tractors.append(tractor)


