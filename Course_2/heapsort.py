# Given an array. Transform it into a minimum heap in-place (you do not have to return anything).

def min_heapify(array, i):
    n = len(array)

    while i < n:
        left = 2 * i + 1
        right = 2 * i + 2
        min_i = i
        if left < n and array[min_i] > array[left]:
            min_i = left
        if right < n and array[min_i] > array[right]:
            min_i = right
        if min_i != i:
            array[min_i], array[i] = array[i], array[min_i]
            i = min_i
        else:
            break


def heapify(array):
    n = len(array)

    #Assuming zero-based indexing (meaning the root node is at index 0),
    # the parent of the ith node is (i-1)/2. So if the n passed to the function
    # is the number of nodes, then the index of the last node is n-1,
    # and the parent of the last node ((n-1)-1)/2 which is the same as n/2 - 1.
    for i in range(n//2 - 1, -1, -1):
        min_heapify(array, i)
    return

def helper_max_heapify(array, i, n):
    while i < n:
        left = 2 * i + 1
        right = 2 * i + 2
        max_i = i
        if left < n and array[max_i] < array[left]:
            max_i = left
        if right < n and array[max_i] < array[right]:
            max_i = right
        if max_i != i:
            array[max_i], array[i] = array[i], array[max_i]
            i = max_i
        else:
            break

def max_heapify(array):
    n = len(array)

    #Assuming zero-based indexing (meaning the root node is at index 0),
    # the parent of the ith node is (i-1)/2. So if the n passed to the function
    # is the number of nodes, then the index of the last node is n-1,
    # and the parent of the last node ((n-1)-1)/2 which is the same as n/2 - 1.
    for i in range(n//2 - 1, -1, -1):
        helper_max_heapify(array, i, n)
    return

def heapsort(array):
    n = len(array)
    max_heapify(array)
    for i in range(n-1, 0, -1):
        print("b:", array)
        array[0], array[i] = array[i], array[0]
        helper_max_heapify(array, 0, len(array[:i]))
        print("a:", array)
    return array

if __name__ == "__main__":
    arr = [3, 2, 1]
    heapify(arr)
    # check that your code works correctly on provided example
    assert arr in [[1, 2, 3], [1, 3, 2]], 'Wrong answer'

    arr = [3, 2, 1, 4]
    # check that your code works correctly on provided example
    assert heapsort(arr) == [1, 2, 3, 4], 'Wrong answer'

    arr = [1, 5, 9, 4, 6, 8, 2, 7, 3]
    # check that your code works correctly on provided example
    assert heapsort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'Wrong answer'