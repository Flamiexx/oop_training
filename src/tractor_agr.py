from src.working_type import WorkingTypeOfTractor


class TractorFinder:
    @staticmethod
    def find_tractor_on_field_by_id(field, tractor_id):
        for tractor in field.tractors:
            if tractor.id == tractor_id:
                return tractor
        return None

    @staticmethod
    def calculate_work_distribution(field):
        total_speed = sum(tractor.processing_speed for tractor in field.tractors)
        work_distribution = {}

        for tractor in field.tractors:
            working_power = tractor.get_working_power()
            work_distribution[tractor.name] = {
                'digging': (working_power['digging'] / total_speed) * 100,
                'sow': (working_power['sow'] / total_speed) * 100,
                'cultivation': (working_power['cultivation'] / total_speed) * 100
            }

        for tractor_name, work in work_distribution.items():
            print(f"{tractor_name} work distribution: Digging {work['digging']:.2f}%, Sow {work['sow']:.2f}%, Cultivation {work['cultivation']:.2f}%")
        return work_distribution

    @staticmethod
    def calculate_time_distribution(field, tractors_together):
        found_tractors = [tractor for tractor in field.tractors if tractor]
        if found_tractors:
            total_speed = sum(tractor.processing_speed for tractor in found_tractors)
            time_to_process = field.size / total_speed
            return time_to_process
        else:
            raise ValueError("No tractors found on the field.")

