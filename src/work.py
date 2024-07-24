class Work:
    def __init__(self):
        self.work = {
            'Digging': 15,
            'Sowing': 35,
            'Cultivating': 25
        }

    def get_work(self, type):
        return self.work.get(type, 0)

