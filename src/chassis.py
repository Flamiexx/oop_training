class Chassis:
    def __init__(self):
        self.chassis = {
            'Easy': 0.5,
            'Middle': 0.3,
            'Heavy': 0.2
        }
        self.max_speed = {
            'Easy': 50,
            'Middle': 30,
            'Heavy': 20
        }

    def get_chassis(self):
        return self.chassis

    def get_chassis_factor(self, type):
        return self.chassis.get(type, 0)

    def get_max_speed(self, type):
        return self.max_speed.get(type, 0)
