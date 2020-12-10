
import unittest
from scripts import example

class GoForIt(unittest.TestCase):

    def test_example_func(self):
        assert example.test_func() == 15
