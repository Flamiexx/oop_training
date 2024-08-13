class WorkDTO:
    def __init__(self, work_type, efficiency):
        self.work_type = work_type
        self.efficiency = efficiency

    def to_dict(self):
        return {'work_type': self.work_type, 'efficiency': self.efficiency}

    @staticmethod
    def from_dict(data):
        return WorkDTO(work_type=data['work_type'], efficiency=data['efficiency'])
