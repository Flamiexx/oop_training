from src.engine_and_chassis import Engine
from src.working_type import WorkingTypeOfTractor


class Tractor:
    def __init__(self, name, engine, chassis_type, tractor_id):
        self.name = name
        self.engine = engine
        self.chassis_type = chassis_type
        self.id = tractor_id
        self.processing_speed = self.engine.get_processing_speed(chassis_type)
        self.working_type = WorkingTypeOfTractor(
            digging=self.processing_speed,
            sow=self.processing_speed,
            cultivation=self.processing_speed
        )

    def get_working_power(self):
        return WorkingTypeOfTractor.adjust_for_chassis(self.chassis_type, self.processing_speed)

    def __str__(self):
        return self.name
