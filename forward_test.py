import unittest
from Incubyte import move_forward 

class TestMoveForward(unittest.TestCase):

    def test_North(self):
        direction = "N"
        position = [0, 0, 0]
        position = move_forward(position, direction)
        self.assertEqual(position, [0, 1, 0])
        

if __name__ == '__main__':
    unittest.main()