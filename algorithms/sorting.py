"""
Сортировки со сложностью O(N^2)
"""

def insertion_sort(array):
    n = len(array)
    for top in range(1, n):
        k = top
        while k > 0 and array[k-1] > array[k]:
            array[k-1], array[k] = array[k], array[k-1]
            k -= 1


def selection_sort(array):
    n = len(array)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]

def bubble_sort(array):
    n = len(array)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]

"""
Сортировки со сложностью O(N)
"""

def counting_sort(array):
    pass

def test_sorting(func):
    orig_lst = [5, 10, 2, 1, 46, 4, 4]
    sorted_lst = [1, 2, 4, 4, 5, 10, 46]
    func(orig_lst)
    assert sorted_lst == orig_lst

if __name__ == '__main__':
    test_sorting(insertion_sort)
    test_sorting(selection_sort)
    test_sorting(bubble_sort)