from src.db_sqlite import Database
from src.engine_service import EngineService
from src.chassis_service import ChassisService
from src.work_service import WorkService
from src.tractor_service import TractorService

# Инициализация базы данных
db = Database('tractors.db')
db.create_tables()

# Инициализация сервисов
engine_service = EngineService(db)
chassis_service = ChassisService(db)
work_service = WorkService(db)
tractor_service = TractorService(db)

# Добавление данных
engine_service.add_engine(100)
chassis_service.add_chassis('Heavy', 0.2)
work_service.add_work('Digging', 15)

# Получение данных по идентификатору
engine = engine_service.get_engine(1)
chassis = chassis_service.get_chassis(1)
work = work_service.get_work(1)

print(engine)  # Output: (1, 100)
print(chassis)  # Output: (1, 'Heavy', 0.2)
print(work)    # Output: (1, 'Digging', 15)

# Добавление трактора
tractor_service.add_tractor('Tractor1', 1, 1, 1)

tractor = tractor_service.get_tractor(1)
print(tractor)  # Output: (1, 'Tractor1', 1, 1, 1)

db.close()