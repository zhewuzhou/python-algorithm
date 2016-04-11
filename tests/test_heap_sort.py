# -*- coding: utf-8 -*-
from sort.heap_sort import heap_sort


def test_heap_sort():
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    heap_sort(a)
    assert a == [1, 2, 3, 4, 5, 6, 7, 8, 9]
