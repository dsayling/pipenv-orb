
import unittest

from scripts import example

class GoForIt(unittest.TestCase):

    def test_example_func(self):
        assert example.test_func(10,5) == 15

    def test_example_func_again(self):
        assert example.test_func(50,25) == 75

    def test_example_func_fail(self):
        try:
            example.test_func()
        except BaseException as e:  # TypeError is raised because we did not pass any args to the function
            assert isinstance(e, TypeError)
