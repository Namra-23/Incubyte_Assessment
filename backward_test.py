import unittest

class TestMoveBackward(unittest.TestCase):

    def test_North(self):
        direction = "N"
        position = [0, 0, 0]
        position = move_backward(position, direction)
        self.assertEqual(position, [0, -1, 0])