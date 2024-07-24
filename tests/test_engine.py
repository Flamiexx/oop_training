import unittest
from src.engine_service import Engine


class TestEngine(unittest.TestCase):

    def setUp(self):
        self.engine = Engine(300)

    def test_get_processing_speed_easy(self):
        speed = self.engine.get_processing_speed('Easy')
        self.assertEqual(speed, 150)  # 300 * 0.5

    def test_get_processing_speed_middle(self):
        speed = self.engine.get_processing_speed('Middle')
        self.assertEqual(speed, 90)  # 300 * 0.3

    def test_get_processing_speed_heavy(self):
        speed = self.engine.get_processing_speed('Heavy')
        self.assertEqual(speed, 60)  # 300 * 0.2


if __name__ == '__main__':
    unittest.main()
