import unittest
from Incubyte import move_forward 

class TestMoveForward(unittest.TestCase):

    def test_North(self):
        direction = "N"
        position = [0, 0, 0]
        position = move_forward(position, direction)
        self.assertEqual(position, [0, 1, 0])
        
    def test_East(self):
        direction = "E"
        position = [0, 0, 0]
        position = move_forward(position, direction)
        self.assertEqual(position, [1, 0, 0])
        
    def test_Up(self):
        direction = "U"
        position = [0, 0, 0]
        position = move_forward(position, direction)
        self.assertEqual(position, [0, 0, 1])
        
    def test_South(self):
        direction = "S"
        position = [0, 0, 0]
        position = move_forward(position, direction)
        self.assertEqual(position, [0, -1, 0])
        
    def test_West(self):
        direction = "W"
        position = [0, 0, 0]
        position = move_forward(position, direction)
        self.assertEqual(position, [-1, 0, 0])
        
    def test_Down(self):
        direction = "D"
        position = [0, 0, 0]
        position = move_forward(position, direction)
        self.assertEqual(position, [0, 0, -1])
        

if __name__ == '__main__':
    unittest.main()