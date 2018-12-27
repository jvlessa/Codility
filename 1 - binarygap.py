def solution(number):
    binary = bin(number)
    string_of_binary = str(binary)[2:]
    array = string_of_binary.split('1')
    new_array = []
    final_number = 0
    
    # See binary gaps and organize them alll
    for item in array:
        if item != '':
            new_array.append('1' + item + '1')

    # Remove last binary gap element if there is no 1 at the end of the string
    if string_of_binary[-1] == '0':
        del new_array[-1]
    
    # Count which one is bigger
    for gap in new_array:
        if len(gap) > final_number:
            final_number = len(gap)

    # Removing only after all process
    if final_number != 0:
        final_number = final_number - 2

    return final_number

#solution(9)
solution(51712)
#solution(561892)