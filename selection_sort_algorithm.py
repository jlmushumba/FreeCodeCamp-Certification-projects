def selection_sort(array):
    if len(array) <= 1:
        return

    # continuously search through a whole list finding the minimum number compared to the current position of the pointer

    current = 0
    the_lowest_number = array[0]
    the_index = 0
    iterations = 0

    while current < len(array) - 1:

        for i in range(current, len(array)):

            if array[i] < the_lowest_number:
                the_lowest_number = array[i]
                the_index = i
        if the_index != current:
            array[current], array[the_index] = array[the_index], array[current]
        current += 1
        the_lowest_number = array[current]
        the_index = current

    return array
