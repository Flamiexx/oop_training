class ChassisDTO:
    def __init__(self, type, factor):
        self.type = type
        self.factor = factor

    def to_dict(self):
        return {'type': self.type, 'factor': self.factor}

    @staticmethod
    def from_dict(data):
        return ChassisDTO(type=data['type'], factor=data['factor'])
