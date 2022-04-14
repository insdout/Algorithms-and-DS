# Given an array of integers sort it in increasing order using the Bubble Sort algorithm.
from random import randint
def BubbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(1, n - i):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            print(array[j-1], array[j], array)
    return array


# Given an array of integers sort it in increasing order using the Insertion Sort algorithm.

def InsertionSort(array):
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i
        while j > 0 and key < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array


# Given an array of integers sort it in increasing order using the Selection Sort algorithm.

def SelectionSort(array:list):
    n = len(array)

    for i in range(n-1):
        min_index = array[i:].index(min(array[i:])) + i
        print("cur_i:", i, "min_index:", min_index, "sel_sort", array)
        array[i], array[min_index] = array[min_index], array[i]
        print("cur_i:",i,"min_index:",min_index,"sel_sort", array)
    return array


def gen_list(n):
    return [randint(-20, 20) for _ in range(n)]

def run_tests (max_len, max_iter):
    for i in range(max_len):
        for _ in range(max_iter):
            arr = gen_list(i)
            assert BubbleSort(arr.copy()) == sorted(arr.copy()), 'Wrong answer. Test: {test}. Answer: {answer}'.format(test=arr, answer=BubbleSort(arr.copy()))
            assert InsertionSort(arr.copy()) == sorted(arr.copy()), 'Wrong answer. Test: {test}. Answer: {answer}'.format(test=arr, answer=InsertionSort(arr.copy()))
            assert SelectionSort(arr.copy()) == sorted(arr.copy()), 'Wrong answer. Test: {test}. Answer: {answer}'.format(test=arr, answer=SelectionSort(arr.copy()))

if __name__ == "__main__":
    arr = [3, 2, 1]
    # check that your code works correctly on provided example
    assert BubbleSort(arr.copy()) == sorted(arr.copy()), 'Wrong answer'
    print(InsertionSort(arr.copy()))
    assert InsertionSort(arr.copy()) == sorted(arr.copy()), 'Wrong answer'
    assert SelectionSort(arr.copy()) == sorted(arr.copy()), 'Wrong answer'

    arr = [3, 2, 1, 15, 14, 13, 12, 0]
    # check that your code works correctly on provided example
    assert BubbleSort(arr.copy()) == sorted(arr.copy()), 'Wrong answer'
    arr = [3, 2, 1, 15, 14, 13, 12, 0]
    print(InsertionSort(arr.copy()))
    assert InsertionSort(arr.copy()) == sorted(arr.copy())
    print(arr)
    print(SelectionSort(arr.copy()))
    assert SelectionSort(arr.copy()) == sorted(arr.copy()), 'Wrong answer'

    run_tests(10, 10)

