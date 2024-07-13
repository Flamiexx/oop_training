from src.field import Field
from src.tractor import Tractor
from src.farm import Farm
from src.tractor_agr import TractorFinder
from src.engine_and_chassis import Engine
farm = Farm(1)

field1 = Field("Field1", 150, 25)
farm.add_field(field1)

engine1 = Engine(300)
engine2 = Engine(250)
engine3 = Engine(200)
engine4 = Engine(150)


tractor1 = Tractor("Tractor1", 1, engine1, 'Middle')
tractor2 = Tractor("Tractor2", 2, engine2, 'Middle')
tractor3 = Tractor("Tractor3", 3, engine3, 'Heavy')
tractor4 = Tractor("Tractor4", 4, engine4, 'Easy')

field1.add_tractor(tractor1)
field1.add_tractor(tractor2)
field1.add_tractor(tractor3)
field1.add_tractor(tractor4)

work_distribution = TractorFinder.calculate_work_distribution(field1)
time_distribution = TractorFinder.calculate_time_distribution(field1, tractors_together=4)

