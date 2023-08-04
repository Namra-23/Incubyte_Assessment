import unittest
from Incubyte import change_direction

class TestChangeDirection(unittest.TestCase):

    # Test cases for rotation in the left direction
    def test_left_North(self):
        # Test changing direction when initially facing North and rotating left
        initial_direction = "N"
        rotate_to = "L"
        self.assertEqual(change_direction(initial_direction, rotate_to), "W")