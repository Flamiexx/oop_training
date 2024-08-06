from src.chassis import Chassis
from src.engine import Engine


class EngineService:
    @staticmethod
    def get_engine_power(engine):
        return engine.get_power()

    @staticmethod
    def increase_power(engine, amount):
        engine.power += amount
        return engine.power

    @staticmethod
    def decrease_power(engine, amount):
        if engine.power - amount >= 0:
            engine.power -= amount
        else:
            engine.power = 0
        return engine.power
