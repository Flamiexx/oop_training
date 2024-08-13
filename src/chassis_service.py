from src.db_sqlite import Database


class ChassisService:
    def __init__(self, db):
        self.db = db

    def add_chassis(self, type, factor):
        query = 'INSERT INTO chassis (type, factor) VALUES (?, ?)'
        self.db.execute_query(query, (type, factor,))

    def get_chassis(self, chassis_id):
        query = 'SELECT * FROM chassis WHERE id = ?'
        result = self.db.fetch_all(query, (chassis_id,))
        return result[0] if result else None
