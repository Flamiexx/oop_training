class Engine:
    def __init__(self, power):
        self.power = power
        self.chassis = {
            'Easy': 0.5,    # посадка 100%, копание 10%, культивация 20%
            'Middle': 0.3,  # посадка 100%, копание 20%, культивация 100%
            'Heavy': 0.2    # для всего 100%
        }

    def get_processing_speed(self, chassis_type):
        if chassis_type not in self.chassis:
            raise ValueError(f"Chassis type '{chassis_type}' not available.")
        return self.power * self.chassis[chassis_type]
