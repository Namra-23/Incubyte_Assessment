def move_forward(position, direction):
    new_position = position.copy()
    if direction == "N":
        new_position[1] += 1
    
    return new_position