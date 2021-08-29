from insertion_sort import __version__


def test_version():
    assert __version__ == '0.1.0'


from insertion_sort.insertion_sort import InsertionSort

def test_random_sorted():
    arr=[8,4,23,42,16,15]
    InsertionSort(arr)
    assert arr[0]==4
    assert arr[1]==8
    assert arr[-1]==42

def test_Reverse_sorted():
    arr=[20,18,12,8,5,-2]
    InsertionSort(arr)
    assert arr[0]==-2
    assert arr[1]==5
    assert arr[-1]==20

def test_Few_uniques():
    arr=[5,15,7,9,9,7]
    InsertionSort(arr)
    assert arr[0]==5
    assert arr[1]==5
    assert arr[-1]==15

def test_Nearly_sorted():
    arr=[5,6,5,7,20,11]
    InsertionSort(arr)
    assert arr[0]==2
    assert arr[1]==3
    assert arr[-1]==20
