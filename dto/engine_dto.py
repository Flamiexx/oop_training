class EngineDTO:
    def __init__(self, power):
        self.power = power

    def to_dict(self):
        return {'power': self.power}

    @staticmethod
    def from_dict(data):
        return EngineDTO(power=data['power'])
