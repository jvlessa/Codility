def cycleRotation(array, rotations):
    for rotation in range(rotations):
        last_element = array[-1]
        del array[-1]
        array = [last_element] + array

    return array

cycleRotation([3, 8, 9, 7, 6], 3)