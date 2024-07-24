from src.field import Field
from src.tractor import Tractor
from src.tractor_service import TractorService


class FieldService(Field):
    def add_tractor(self, tractor):
        if len(self.tractors) < 4:
            self.tractors.append(tractor)

    def get_tractors(self):
        def format_tractor(tractor):
            return f'id: {tractor.id}, {tractor.name}'

        return list(map(format_tractor, self.tractors))

    def info_about_field(self):
        tractor_names = '\n'.join(self.get_tractors()) or "No tractors"
        return f'Field name: {self.name}\nField size: {self.size}\n{tractor_names}'
