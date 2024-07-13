class WorkingTypeOfTractor:
    def __init__(self, digging, sow, cultivation):
        self.digging = digging          # копание
        self.sow = sow                  # посадка
        self.cultivation = cultivation  # культивация

    @staticmethod
    def adjust_for_chassis(chassis_type, power):
        chassis_efficiency = {
            'Easy': {'digging': 0.1, 'sow': 1.0, 'cultivation': 0.2},
            'Middle': {'digging': 0.2, 'sow': 1.0, 'cultivation': 1.0},
            'Heavy': {'digging': 1.0, 'sow': 1.0, 'cultivation': 1.0}
        }

        if chassis_type not in chassis_efficiency:
            raise ValueError(f"Chassis type '{chassis_type}' not available.")

        efficiency = chassis_efficiency[chassis_type]

        adjusted_power = {
            'digging': power * efficiency['digging'],
            'sow': power * efficiency['sow'],
            'cultivation': power * efficiency['cultivation']
        }

        return adjusted_power
