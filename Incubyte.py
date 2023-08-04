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
    
    return new_position