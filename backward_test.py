import unittest
from Incubyte import move_backward

class TestMoveBackward(unittest.TestCase):

    def test_North(self):
        direction = "N"
        position = [0, 0, 0]
        position = move_backward(position, direction)
        self.assertEqual(position, [0, -1, 0])
        
    def test_East(self):
        direction = "E"
        position = [0, 0, 0]
        position = move_backward(position, direction)
        self.assertEqual(position, [-1, 0, 0])
        
if __name__ == '__main__':
    unittest.main()