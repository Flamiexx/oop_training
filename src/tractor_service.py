from src.work import Work
from src.work_service import Work
from src.field import Field
from src.chassis import Chassis
from src.tractor import Tractor
from src.engine_service import Engine


class TractorService:
    @staticmethod
    def calculate_speed(tractor, work_service):
        chassis_factor = tractor.chassis.get_chassis_factor(tractor.chassis_type)
        work_factor = work_service.work.get_work(tractor.work_type)

        if work_factor == 0:
            raise ValueError(f"Work factor for type '{tractor.work_type}' is zero.")

        speed = (tractor.engine.get_power() * chassis_factor) / work_factor

        max_speed = tractor.chassis.get_max_speed(tractor.chassis_type)
        if speed > max_speed:
            raise ValueError(f"Calculated speed {speed:.2f} exceeds the maximum allowed speed {max_speed} "
                             f"for chassis type '{tractor.chassis_type}'")

        return speed
