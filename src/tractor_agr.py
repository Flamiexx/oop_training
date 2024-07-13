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
            work_distribution[tractor.name] = (tractor.processing_speed / total_speed) * 100

        for tractor_name, percentage in work_distribution.items():
            print(f"{tractor_name} will work on {percentage:.2f}% of the field.")
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
