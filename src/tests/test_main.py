import unittest

from src import main


# mock requests out of tests
class DummyTest(unittest.TestCase):
    def test_dummy(self):
        dummy = main.main()
        expected = "Kingdom Come: Deliverance II"
        self.assertEqual(dummy, expected)


if __name__ == "__main__":
    unittest.main()
