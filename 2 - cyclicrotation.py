def cycleRotation(array, rotations):
    if len(array) > 0:
        for rotation in range(rotations):
            last_element = array[-1]
            del array[-1]
            array = [last_element] + array
    return array

cycleRotation([], 3)