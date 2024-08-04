from src.work import Work


class WorkService:
    def __init__(self):
        self.work = Work()

    def add_work(self, work_type, factor):
        """Add a new type of work with its efficiency factor."""
        if work_type in self.work.work:
            raise ValueError(f"Work type '{work_type}' already exists.")
        self.work.work[work_type] = factor

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