from dto.engine_dto import EngineDTO
from dto.chassis_dto import ChassisDTO
from dto.work_dto import WorkDTO


class TractorDTO:
    def __init__(self, name, engine, chassis, work, id):
        self.name = name
        self.engine = engine
        self.chassis = chassis
        self.work = work
        self.id = id

    def to_dict(self):
        return {
            'name': self.name,
            'engine': self.engine.to_dict(),
            'chassis': self.chassis.to_dict(),
            'work': self.work.to_dict(),
            'id': self.id
        }

    @staticmethod
    def from_dict(data):
        return TractorDTO(
            name=data['name'],
            engine=EngineDTO.from_dict(data['engine']),
            chassis=ChassisDTO.from_dict(data['chassis']),
            work=WorkDTO.from_dict(data['work']),
            id=data['id']
        )
