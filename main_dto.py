from src.tractor import Tractor
from src.engine_service import Engine
from dto.engine_dto import EngineDTO
from src.work import Work
from dto.work_dto import WorkDTO
from src.chassis import Chassis
from dto.chassis_dto import ChassisDTO
from dto.tractor_dto import TractorDTO


# Создание объектов основных классов
engine = Engine(power=100)
chassis = ChassisDTO(type='Heavy', factor=0.2)
work = WorkDTO(work_type='Digging', efficiency=15)
tractor = TractorDTO(name='Tractor1', engine=engine, chassis=chassis, work=work, id=1)

# Создание DTO объекта
tractor_dto = TractorDTO(
    name=tractor.name,
    engine=EngineDTO(tractor.engine.get_power()),
    chassis=ChassisDTO(type=tractor.chassis.type, factor=tractor.chassis.factor),
    work=WorkDTO(work_type=tractor.work.work_type, efficiency=tractor.work.efficiency),
    id=tractor.id
)

# Сериализация
tractor_data = tractor_dto.to_dict()

# Десериализация
tractor_obj = TractorDTO.from_dict(tractor_data)
