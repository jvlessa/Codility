# Odds are integer numbers that which is not a multiple of two (impar)

def oddoccurrencesinarray(array):
    unpaired = None
    
    for chosen in array:
        counter = 0
        for element in array:
            if chosen == element:
                counter += 1
        if counter == 1:
            unpaired = chosen

    return unpaired

oddoccurrencesinarray([9, 3, 9, 3, 9, 7, 9])