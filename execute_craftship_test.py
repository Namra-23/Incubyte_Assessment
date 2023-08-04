import unittest

class TestExecuteCommands(unittest.TestCase):

    def test_single_command_forward_North(self):
        commands = ["f"]
        initial = {
            "position": [0, 0, 0],
            "direction": "N",
        }
        expected = {
            "position": [0, 1, 0],
            "direction": "N",
        }
        actual = execute_commands(commands, initial)
        self.assertEqual(actual, expected)