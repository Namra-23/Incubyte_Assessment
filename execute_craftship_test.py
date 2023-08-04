import unittest
from Incubyte import execute_commands

class TestExecuteCommands(unittest.TestCase):

    def test_single_command_forward_North(self):
        commands = ["f"]
        initial = {
            "position": [0, 0, 0],
            "direction": "N"
        }
        expected = {
            "position": [0, 1, 0],
            "direction": "N"
        }
        actual = execute_commands(commands, initial)
        self.assertEqual(actual, expected)
        
    def test_base_test_case(self):
        commands = ["f", "r", "u", "b", "l"]
        initial = {
            "position": [0, 0, 0],
            "direction": "N",
        }
        expected = {
            "position": [0, 1, -1],
            "direction": "W",
        }
        actual = execute_commands(commands, initial)
        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main()