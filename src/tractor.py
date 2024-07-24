from src.engine_service import Engine
from src.work import Work


class Tractor:
    def __init__(self, name, engine, chassis, chassis_type, id, work, work_type):
        self.name = name
        self.engine = engine
        self.chassis = chassis
        self.chassis_type = chassis_type
        self.work = work
        self.work_type = work_type
        self.id = id

    def __str__(self):
        return self.name
