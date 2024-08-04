class Chassis:
    def __init__(self):
        self._chassis = {
            'Easy': 0.5,
            'Middle': 0.3,
            'Heavy': 0.2
        }
        self._max_speed = {
            'Easy': 50,
            'Middle': 30,
            'Heavy': 20
        }

    @property
    def chassis(self):
        return self._chassis

    @property
    def max_speed(self):
        return self._max_speed

    def get_chassis_factor(self, type):
        return self._chassis.get(type, 0)

    def get_max_speed(self, type):
        return self._max_speed.get(type, 0)
