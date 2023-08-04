# Incubyte_Assessment

# Crafter Space Exploration

This repository contains Python code for a Crafter Space Exploration project. The project involves moving a spacecraft in different directions and changing its orientation.

## Getting Started

To run the project, you will need Python installed on your system. Clone the repository to your local machine and use the following instructions to execute the commands.

## Usage

The main functionality is defined in the `Incubyte.py` file. It provides the following functions:

### move_forward(position, direction)

Function for handling forward direction. It takes the current position and direction of the spacecraft as input and returns the new position after moving one step forward in the given direction.

### move_backward(position, direction)

Function for handling backward direction. It takes the current position and direction of the spacecraft as input and returns the new position after moving one step backward in the given direction.

### change_direction(initial_direction, rotate_to)

Function for handling direction changes. It takes the initial direction of the spacecraft and the rotation instruction (L for left, R for right) as input and returns the new direction after the rotation.

### execute_commands(commands, initial)

Function to execute a series of commands on the spacecraft. It takes a string of commands and the initial position and direction as input and returns the final position and direction after executing all the commands.

## Running Tests

The repository also includes test files to validate the correctness of the functions. The test files are named `forward_test.py`, `backward_test.py`, `direction_changed_test.py` and `execute_crafship_test.py`. To run the tests, use the following commands:
For forward_test.py:                 python -m unittest forward_test.py
For backward_test.py:                python -m unittest backward_test.py
For direction_changed_test.py:       python -m unittest direction_changed_test.py
For execute_craftship_test.py:       python -m unittest execute_craftship_test.py


## Contributing

Contributions to this project are welcome. If you find any issues or have improvements to suggest, please feel free to open a pull request.
