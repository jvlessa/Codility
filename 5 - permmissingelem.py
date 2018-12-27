def solution(array):
    array.sort()
    missing = None

    counter = 1
    for i in array:
        if i + 1 != array[counter]:
            missing = i - 1
        if missing == None:
            counter += 1

    return missing

solution([2, 3, 1, 5])