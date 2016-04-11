from utils.random_partition import random_partition
from math import floor


def quick_select(arr, start, end, nth):
    i = random_partition(arr, start, end)
    print(arr, "\n")
    print("xxxx", "aa", start, "end", end, "nth", nth, "i", i, "\n")
    if nth == i:
        return arr[i]
    elif nth < i:
        return quick_select(arr, start, i, nth)
    else:
        return quick_select(arr, i, end, nth)
