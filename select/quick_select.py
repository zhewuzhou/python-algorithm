from utils.random_partition import random_partition


def quick_select(arr, start, end, nth):
    partition = random_partition(arr, start, end)
    relative_nth = partition - start + 1
    if nth == relative_nth:
        return arr[partition]
    elif nth < relative_nth:
        return quick_select(arr, start, partition - 1, nth)
    else:
        return quick_select(arr, partition + 1, end, nth - relative_nth)
