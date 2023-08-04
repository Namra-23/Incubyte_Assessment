import unittest
from Incubyte import change_direction

class TestChangeDirection(unittest.TestCase):

    # Test cases for rotation in the left direction
    def test_left_North(self):
        # Test changing direction when initially facing North and rotating left
        initial_direction = "N"
        rotate_to = "L"
        self.assertEqual(change_direction(initial_direction, rotate_to), "W")
    
    def test_left_South(self):
        # Test changing direction when initially facing South and rotating left
        initial_direction = "S"
        rotate_to = "L"
        self.assertEqual(change_direction(initial_direction, rotate_to), "E")
        
    def test_left_East(self):
        # Test changing direction when initially facing East and rotating left
        initial_direction = "E"
        rotate_to = "L"
        self.assertEqual(change_direction(initial_direction, rotate_to), "N")

    def test_left_West(self):
        # Test changing direction when initially facing West and rotating left
        initial_direction = "W"
        rotate_to = "L"
        self.assertEqual(change_direction(initial_direction, rotate_to), "S")
        
    def test_left_Up(self):
        # Test changing direction when initially facing Up and rotating left
        initial_direction = "U"
        rotate_to = "L"
        self.assertEqual(change_direction(initial_direction, rotate_to), "W")

    def test_left_Down(self):
        # Test changing direction when initially facing Down and rotating left
        initial_direction = "D"
        rotate_to = "L"
        self.assertEqual(change_direction(initial_direction, rotate_to), "E")
        
    # Test cases for rotation in the right direction
    def test_right_North(self):
        # Test changing direction when initially facing North and rotating right
        initial_direction = "N"
        rotate_to = "R"
        self.assertEqual(change_direction(initial_direction, rotate_to), "E")

    def test_right_South(self):
        # Test changing direction when initially facing South and rotating right
        initial_direction = "S"
        rotate_to = "R"
        self.assertEqual(change_direction(initial_direction, rotate_to), "W")
        
    def test_right_East(self):
        # Test changing direction when initially facing East and rotating right
        initial_direction = "E"
        rotate_to = "R"
        self.assertEqual(change_direction(initial_direction, rotate_to), "S")

    def test_right_West(self):
        # Test changing direction when initially facing West and rotating right
        initial_direction = "W"
        rotate_to = "R"
        self.assertEqual(change_direction(initial_direction, rotate_to), "N")