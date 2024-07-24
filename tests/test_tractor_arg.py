import unittest
from src.field import Field
from src.tractor import Tractor
from src.engine_service import Engine
from src.tractor_agr import TractorFinder


class TestTractorFinder(unittest.TestCase):

    def setUp(self):
        self.field = Field("Field1", 100)
        engine1 = Engine(300)
        engine2 = Engine(250)
        engine3 = Engine(200)
        engine4 = Engine(150)
        self.tractor1 = Tractor("Tractor1", engine1, 'Easy', 1)
        self.tractor2 = Tractor("Tractor2", engine2, 'Middle', 2)
        self.tractor3 = Tractor("Tractor3", engine3, 'Heavy', 3)
        self.tractor4 = Tractor("Tractor4", engine4, 'Easy', 4)
        self.field.add_tractor(self.tractor1)
        self.field.add_tractor(self.tractor2)
        self.field.add_tractor(self.tractor3)
        self.field.add_tractor(self.tractor4)

    def test_find_tractor_on_field(self):
        found_tractor = TractorFinder.find_tractor_on_field_by_id(self.field, self.tractor3.id)
        self.assertIsNotNone(found_tractor)
        self.assertEqual(found_tractor.name, "Tractor3")

    def test_calculate_work_distribution(self):
        work_distribution = TractorFinder.calculate_work_distribution(self.field)
        self.assertIn("Tractor1", work_distribution)
        self.assertIn("Tractor2", work_distribution)
        self.assertIn("Tractor3", work_distribution)
        self.assertIn("Tractor4", work_distribution)


if __name__ == '__main__':
    unittest.main()
