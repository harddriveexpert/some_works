import copy
import SortingModule
import time


def direct_search(array,find_word):
    f = 0
    for i in range(len(array)):
        if array[i] == find_word:
            f = i
            break
    time.sleep(0.0001)
    return f


def binar_search(array, find_word):
    midel = len(array) // 2
    start = 0
    end = len(array) - 1
    while find_word != array[midel] and start <= end:
        if array[midel] > find_word:
            end = midel - 1
        else:
            start = midel + 1
        midel = (end + start) // 2
    time.sleep(0.0001)
    if end >= start:
        return midel
    else:
        return -1


def binar_search_with_sortind(array, find_word):
    merge = SortingModule.merge_sort(copy.deepcopy(array))

    midel = len(merge) // 2
    start = 0
    end = len(merge) - 1
    while find_word != merge[midel] and start <= end:
        if merge[midel] > find_word:
            end = midel - 1
        else:
            start = midel + 1
        midel = (end + start) // 2
    time.sleep(0.0001)
    if end >= start:
        return midel
    else:
        return -1



