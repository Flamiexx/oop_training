class Field:
    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.tractors = []

    def add_tractor(self, tractor):
        if len(self.tractors) < 4:
            self.tractors.append(tractor)
        else:
            raise ValueError('Haven`t place for more tractors')

    def get_tractors(self):
        def format_tractor(tractor):
            return f'id: {tractor.id}, {tractor.name}'

        return list(map(format_tractor, self.tractors))

    def info_about_field(self):
        tractor_names = '\n'.join(self.get_tractors()) or "No tractors"
        return f'Field name: {self.name}\nField size: {self.size}\n{tractor_names}'
