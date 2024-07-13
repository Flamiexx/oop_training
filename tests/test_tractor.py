import unittest
from src.tractor import Tractor
from src.engine_and_chassis import Engine


class TestTractor(unittest.TestCase):

    def setUp(self):
        engine = Engine(300)
        self.tractor = Tractor("Tractor1", engine, 'Easy', 1)

    def test_tractor_initialization(self):
        self.assertEqual(self.tractor.name, "Tractor1")
        self.assertEqual(self.tractor.engine.power, 300)
        self.assertEqual(self.tractor.chassis_type, 'Easy')


if __name__ == '__main__':
    unittest.main()
