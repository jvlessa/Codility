def solution(X, A):        
    iterations = 0
    leaves = []

    for i in A:
        leaves.append(i)
        leaves = sorted(leaves)
        no_duplicates = list(set(leaves)) # remove duplicated but turns the list to an object, so we had to convert back to list
        is_sequence = verify_sequence(no_duplicates) # verify if the numbers are a sequence or not

        if is_sequence == True and len(no_duplicates) == X:
            return iterations

        iterations = iterations + 1

    return -1

def verify_sequence(B):
    result = True

    if len(B) > 1:
        iterations = 0

        for i in B:
            if iterations > 0:
                if i - 1 != B[iterations - 1]:
                    result = False
            iterations = iterations + 1

    return result

result = solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
result1 = solution(1, [1])
result2 = solution(2, [1, 2])
result3 = solution(5, [1, 3, 4, 6])
done = True