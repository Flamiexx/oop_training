from src.chassis import Chassis
from src.engine import Engine
from src.db_sqlite import Database


class EngineService:

    def __init__(self, db):
        self.db = db

    def add_engine(self, power):
        query = 'INSERT INTO engines (power) VALUES (?)'
        self.db.execute_query(query, (power,))

    def get_engine(self, engine_id):
        query = 'SELECT * FROM engines WHERE id = ?'
        result = self.db.fetch_all(query, (engine_id,))
        return result[0] if result else None

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
