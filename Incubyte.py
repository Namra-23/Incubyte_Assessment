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
    # For left rotation
    if rotate_to == "L":
        if initial_direction == "N":
            return "W"
        elif initial_direction == "S":
            return "E"
        elif initial_direction == "E":
            return "N"
        elif initial_direction == "W":
            return "S"
        elif initial_direction == "U":
            return "W"
        elif initial_direction == "D":
            return "E"
    # For right rotation 
    elif rotate_to == "R":
        if initial_direction == "N":
            return "E"
        elif initial_direction == "S":
            return "W"