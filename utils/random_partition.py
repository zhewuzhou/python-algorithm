import random


def random_partition(arr, start, end):
    i = random.randint(start, end)
    arr[end], arr[i] = arr[i], arr[end]
    return __partition(arr, start, end)


def __partition(arr, start, end):
    i = start - 1
    for j in range(start, end):
        if arr[j] <= arr[end]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
