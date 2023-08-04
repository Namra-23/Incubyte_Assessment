# Function for handling forward direction
def move_forward(position, direction):
    new_position = position.copy()
    if direction == "N":
        new_position[1] += 1
    elif direction == "E":
        new_position[0] += 1
    elif direction == "U":
        new_position[2] += 1
    elif direction == "S":
        new_position[1] -= 1
    elif direction == "W":
        new_position[0] -= 1
    elif direction == "D":
        new_position[2] -= 1
    
    return new_position

# Function for handling backward direction
def move_backward(position, direction):
    new_position = position.copy()
    if direction == "N":
        new_position[1] -= 1
    elif direction == "E":
        new_position[0] -= 1
    elif direction == "U":
        new_position[2] -= 1
    elif direction == "S":
        new_position[1] += 1
    elif direction == "W":
        new_position[0] += 1
    elif direction == "D":
        new_position[2] += 1
    
    return new_position


# Function for handling direction changed
def change_direction(initial_direction, rotate_to):
    # Define a dictionary to handle the direction changes
    direction_changes = {
        "NL": "W",  # North to Left becomes West
        "SL": "E",  # South to Left becomes East
        "EL": "N",  # East to Left becomes North
        "WL": "S",  # West to Left becomes South
        "UL": "W",  # Up to Left becomes West
        "DL": "E",  # Down to Left becomes East
        "NR": "E",  # North to Right becomes East
        "SR": "W",  # South to Right becomes West
        "ER": "S",  # East to Right becomes South
        "WR": "N",  # West to Right becomes North
        "UR": "E",  # Up to Right becomes East
        "DR": "W",  # Down to Right becomes West
    }

    # Create a key based on the initial direction and rotation instruction
    key = initial_direction + rotate_to

    # If the key is in the dictionary, return the resulting direction
    if key in direction_changes:
        return direction_changes[key]

    # If the key is not in the dictionary, return the initial direction (no rotation)
    return initial_direction


# Code to execute Command

def execute_commands(commands, initial):
    position = initial["position"].copy()
    direction = initial["direction"]

    for command in commands:
        if command == "f":
            position = move_forward(position, direction)
        elif command == "b":
            position = move_backward(position, direction)
        elif command == "r":
            direction = change_direction(direction, "R")
        elif command == "l":
            direction = change_direction(direction, "L")
        elif command == "u":
            position[2] += 1
        elif command == "d":
            position[2] -= 1

    return {
        "position": position,
        "direction": direction,
    }