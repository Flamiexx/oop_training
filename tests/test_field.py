import unittest
from src.field import Field
from src.tractor import Tractor
from src.engine_and_chassis import Engine  # Make sure to import from the correct module


class TestField(unittest.TestCase):

    def setUp(self):
        self.field = Field("Field1", 100)
        engine = Engine(300)
        self.tractor = Tractor("Tractor1", engine, 'Easy', 1)

    def test_add_tractor(self):
        self.field.add_tractor(self.tractor)
        self.assertEqual(len(self.field.tractors), 1)

    def test_info_about_field(self):
        self.field.add_tractor(self.tractor)
        info = self.field.info_about_field()
        self.assertIn("Field name: Field1", info)
        self.assertIn("Field size: 100", info)
        self.assertIn("Tractor1", info)


if __name__ == '__main__':
    unittest.main()

