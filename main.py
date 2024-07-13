from src.field import Field
from src.tractor import Tractor
from src.engine_and_chassis import Engine
from src.tractor_agr import TractorFinder


field1 = Field("Field1", 150)

engine1 = Engine(300)
engine2 = Engine(400)
engine3 = Engine(500)
engine4 = Engine(600)

tractor1 = Tractor("Tractor1", engine1, 'Easy', 1)
tractor2 = Tractor("Tractor2", engine2, 'Middle', 2)
tractor3 = Tractor("Tractor3", engine3, 'Heavy', 3)
tractor4 = Tractor("Tractor4", engine4, 'Easy', 4)

field1.add_tractor(tractor1)
field1.add_tractor(tractor2)
field1.add_tractor(tractor3)
field1.add_tractor(tractor4)

work_distribution = TractorFinder.calculate_work_distribution(field1)
print(work_distribution)
