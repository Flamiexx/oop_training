class Engine:
    def __init__(self, power):
        self._power = power

    def get_power(self):
        return self._power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value
