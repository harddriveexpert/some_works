import StudentClass
import copy

def selection_sort(data):
    array = copy.deepcopy(data)
    i = 0
    while i < len(array) - 1:
        smal = i
        j = i + 1
        while j < len(array):
            if array[j].__lt__(array[smal]):
                smal = j
            j += 1
        array[i], array[smal] = array[smal], array[i]
        i += 1
    return array

def HeapSort(lst):
    data=copy.deepcopy(lst)
    for i in range((len(data) - 2) // 2, -1, -1):
        HeapSift(data, i, len(data) - 1)
    for end in range(len(data) - 1, 0, -1):
        data[end], data[0] = data[0], data[end]
        HeapSift(data, 0, end - 1)
    return data

def HeapSift(data, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if ((child + 1) <= end) and (data[child].__lt__(data[child + 1]) ):
            child += 1
        if data[root].__lt__(data[child]):
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break


def merge(left, right): #сортировка слиянием
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].__le__(right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:] + right[j:]
    return res

def merge_sort(lst):
    array = copy.deepcopy(lst)
    if len(array) <= 1:
        return array
    else:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]
    return merge(merge_sort(left), merge_sort(right))