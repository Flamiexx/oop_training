class Tractor:
    def __init__(self, name, engine, chassis_type, tractor_id):
        self.name = name
        self.engine = engine
        self.chassis_type = chassis_type
        self.id = tractor_id
        self.processing_speed = self.engine.get_processing_speed(chassis_type)

    def __str__(self):
        return self.name
