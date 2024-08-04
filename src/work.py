class Work:
    def __init__(self):
        self._work = {
            'Digging': 15,
            'Sowing': 35,
            'Cultivating': 25
        }

    @property
    def work(self):
        return self._work

    def get_work(self, type):
        return self._work.get(type, 0)
