class Tractor:
    def __init__(self, name, engine, chassis, chassis_type, id, work, work_type):
        self._name = name
        self._engine = engine
        self._chassis = chassis
        self._chassis_type = chassis_type
        self._id = id
        self._work = work
        self._work_type = work_type

    @property
    def name(self):
        return self._name

    @property
    def engine(self):
        return self._engine

    @property
    def chassis(self):
        return self._chassis

    @property
    def chassis_type(self):
        return self._chassis_type

    @property
    def id(self):
        return self._id

    @property
    def work(self):
        return self._work

    @property
    def work_type(self):
        return self._work_type

    @name.setter
    def name(self, value):
        self._name = value

    @engine.setter
    def engine(self, value):
        self._engine = value

    @chassis_type.setter
    def chassis_type(self, value):
        self._chassis_type = value

    @id.setter
    def id(self, value):
        self._id = value

    @work_type.setter
    def work_type(self, value):
        self._work_type = value

    def __str__(self):
        return self._name
