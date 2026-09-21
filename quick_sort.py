def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    sublist_1 = [num for num in array if num < pivot]
    sublist_2 = [num for num in array if num == pivot]
    sublist_3 = [num for num in array if num > pivot]
    sublist_1 = quick_sort(sublist_1)
    #sublist_2 = quick_sort(sublist_2)
    sublist_3 = quick_sort(sublist_3)

    return sublist_1 + sublist_2 + sublist_3
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))

