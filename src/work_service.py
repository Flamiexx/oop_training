from src.work import Work
from src.db_sqlite import Database


class WorkService:
    def __init__(self, db):
        self.db = db
        self.work = Work()

    def add_work(self, work_type, efficiency):
        query = 'INSERT INTO works (work_type, efficiency) VALUES (?, ?)'
        self.db.execute_query(query, (work_type, efficiency,))

    def get_work(self, work_id):
        query = 'SELECT * FROM works WHERE id = ?'
        result = self.db.fetch_all(query, (work_id,))
        return result[0] if result else None

    def update_work_factor(self, work_type, new_factor):
        """Update the efficiency factor of an existing type of work."""
        if work_type not in self.work.work:
            raise ValueError(f"Work type '{work_type}' does not exist.")
        self.work.work[work_type] = new_factor

    def delete_work(self, work_type):
        """Delete an existing type of work."""
        if work_type not in self.work.work:
            raise ValueError(f"Work type '{work_type}' does not exist.")
        del self.work.work[work_type]