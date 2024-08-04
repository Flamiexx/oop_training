class Engine:
    def __init__(self, power):
        self._power = power  # Приватный атрибут

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if value < 0:
            raise ValueError("Power cannot be negative")
        self._power = value

    def get_power(self):
        return self._power
