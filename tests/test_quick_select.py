from select.quick_select import quick_select


def test_quick_select():
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    assert quick_select(arr, 0, 7, 4) == 5
