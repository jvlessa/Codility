def solution(a):
    final_value = 0
    iterations = 0

    for item in a:
        if iterations > 0: # starts to run the process only after first item of array
            first = sum_items(a[:iterations])
            second = sum_items(a[iterations:])
            result = first - second

            # if it is a negative number, does not matter, we just need to know the difference
            if result < 0:
                result = result * -1

            #print(result)

            # first result will always replace the final value 
            if iterations == 1:
                final_value = result
            # if iterations comes after the first one, it will replace the final value only if the result is smaller
            else:
                if result < final_value:
                    final_value = result

        # adding one to the iterations counter
        iterations = iterations + 1

    return final_value

def sum_items(b):
    value = 0
    for i in b:
        value = value + i
    return value


solution([3, 1, 2, 4, 3])