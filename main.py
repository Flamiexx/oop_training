from src.tractor import Tractor
from src.engine_service import Engine
from src.tractor_service import TractorService
from src.work import Work
from src.field import Field
from src.chassis import Chassis
from src.work_service import WorkService
from src.engine_service import EngineService


field1 = Field("Field1", 150, 1)
engine1 = Engine(3000)
# engine2 = Engine(3000)
# engine3 = Engine(3000)
chassis1 = Chassis()
work1 = Work()
engine_service = EngineService()

tractor1 = Tractor("Tractor1", engine1, chassis1, 'Heavy', 1, work1, 'Sowing')
# tractor2 = Tractor("Tractor1", engine2, chassis1, 'Middle', 1, work1, 'Sowing')
# tractor3 = Tractor("Tractor1", engine3, chassis1, 'Easy', 1, work1, 'Sowing')
engine_service.increase_power(engine1, 6)

tractor_service = TractorService()
work_service = WorkService()

speed1 = tractor_service.calculate_speed(tractor1, work_service)
# speed2 = tractor_service.calculate_speed(tractor2, work_service)
# speed3 = tractor_service.calculate_speed(tractor3, work_service)
print(f"The speed of {tractor1.name} is {speed1}")
# print(f"The speed of {tractor2.name} is {speed2}")
# print(f"The speed of {tractor3.name} is {speed3}")
