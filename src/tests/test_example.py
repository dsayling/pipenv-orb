
import unittest
import scripts

class GoForIt(unittest.TestCase):

    def test_example_func(self):
        assert scripts.test_func() == 15
