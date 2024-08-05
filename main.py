from src.tractor import Tractor
from src.engine_service import Engine
from src.tractor_service import TractorService
from src.work import Work
from src.field import Field
from src.chassis import Chassis


field1 = Field("Field1", 150, 1)
engine1 = Engine(3000)
engine2 = Engine(3000)
engine3 = Engine(3000)
chassis1 = Chassis()
work1 = Work()


tractor1 = Tractor("Tractor1", engine1, chassis1, 'Heavy', 1, work1, 'Sowing')
tractor3 = Tractor("Tractor1", engine2, chassis1, 'Middle', 1, work1, 'Sowing')
tractor2 = Tractor("Tractor1", engine3, chassis1, 'Easy', 1, work1, 'Sowing')


tractor_service = TractorService()
speed1 = tractor_service.calculate_speed(tractor1)
speed2 = tractor_service.calculate_speed(tractor2)
speed3 = tractor_service.calculate_speed(tractor3)
print(f"The speed of {tractor1.name} is {speed1}")
print(f"The speed of {tractor2.name} is {speed2}")
print(f"The speed of {tractor3.name} is {speed3}")
# chassis = Chassis('Easy')
# engine1 = Engine(3000)
# engine2 = Engine(400)
# engine3 = Engine(500)
# engine4 = Engine(600)
#
# tractor1 = Tractor("Tractor1", engine1, chassis, 1, work)
# # tractor2 = Tractor("Tractor2", engine2, 'Middle', 2, work)
# # tractor3 = Tractor("Tractor3", engine3, 'Heavy', 3, work)
# # tractor4 = Tractor("Tractor4", engine4, 'Easy', 4, work)
# tractor_service = TractorService()
# work_type = 'Digging'
# speed = tractor_service.calculate_speed(tractor1)
# print(f"Speed of {tractor1.name} for {work_type}: {speed}")
#

# field1.add_tractor(tractor1)
# field1.add_tractor(tractor2)
# field1.add_tractor(tractor3)
# field1.add_tractor(tractor4)
