def solution(A):
    result = 1
    ordered = sorted(A)

    iterations = 0

    for i in ordered:
        if iterations > 0:
            if i - 1 != ordered[iterations - 1]:
                result = 0

        iterations = iterations + 1 

    return result

#solution([4, 1, 3, 2])
solution([4, 1, 3])