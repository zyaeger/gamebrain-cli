import unittest

from src import main


class DummyTest(unittest.TestCase):
    def test_dummy(self):
        dummy = main.main()
        self.assertTrue(dummy)


if __name__ == "__main__":
    unittest.main()
