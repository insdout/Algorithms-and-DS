# Need to fix partition function!!!

# Given an array and a pivot element index, implement the partition function:
# move all the elements smaller than pivot element to the left of it and all the elements larger than it to the right.
# Return the array after partition.

def partition_h(a, left, right):
    pivot = left
    while left < right:
        while a[left] <= a[pivot] and left < len(a)-1:
            left += 1
        while a[right] > a[pivot] and right > 0: #why not >=?: swap right=pivot with pivot
            right -= 1
        if left < right:
            a[left], a[right] = a[right], a[left]
    a[pivot], a[right] = a[right], a[pivot]
    return right


def partition(array, pivot_index):
    n = len(array)
    if pivot_index != 0:
        array[pivot_index], array[0] = array[0], array[pivot_index]
    return partition_h(array, 0, n-1)

def partition2(array, pivot_index):
    n = len(array)
#    pivot = array[pivot_index]

    if array[pivot_index] == max(array):
        array[-1], array[pivot_index] = array[pivot_index], array[-1]
        return array

    if pivot_index != 0:
        array[0], array[pivot_index] = array[pivot_index], array[0]
    pivot = array[0]

    # YOUR CODE GOES HERE
    l = 1
    r = n-1

    while l <= r:
        while l < r and array[l] < pivot:
            l += 1
        while r >= l and array[r] >= pivot:
            r -= 1
        if l < r:
            array[l], array[r] = array[r], array[l]

    if r != 0:
        array[0], array[r] = array[r], array[0]

    return array

if __name__ == "__main__":
    arr = [3, 2]
    pivot_index = 0
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[2, 3]], 'Wrong answer'
    assert partition2(arr.copy(), pivot_index) in [[2, 3]], 'Wrong answer'

    arr = [3, 2]
    pivot_index = 1
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[2, 3]], 'Wrong answer'
    assert partition2(arr.copy(), pivot_index) in [[2, 3]], 'Wrong answer'

    arr = [3, 2, 1]
    pivot_index = 0
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[1, 2, 3]], 'Wrong answer'
    assert partition2(arr.copy(), pivot_index) in [[1, 2, 3]], 'Wrong answer'

    arr = [3, 2, 1]
    pivot_index = 1
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[1, 2, 3]], 'Wrong answer'
    assert partition2(arr.copy(), pivot_index) in [[1, 2, 3]], 'Wrong answer'

    arr = [3, 2, 1]
    pivot_index = 2
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[1, 2, 3]], 'Wrong answer'
    assert partition2(arr.copy(), pivot_index) in [[1, 2, 3]], 'Wrong answer'


    arr = [3, 2, 1, 4]
    pivot_index = 0
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4]], 'Wrong answer'
    assert partition(arr.copy(), pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4]], 'Wrong answer'

    arr = [3, 2, 1, 4]
    pivot_index = 1
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4]], 'Wrong answer'
    assert partition2(arr.copy(), pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4]], 'Wrong answer'

    arr = [3, 2, 1, 4]
    pivot_index = 2
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4]], 'Wrong answer'
    assert partition2(arr.copy(), pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4]], 'Wrong answer'

    arr = [3, 2, 1, 4]
    pivot_index = 3
    # check that your code works correctly on provided example
    assert partition(arr.copy(), pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4]], 'Wrong answer'
    assert partition2(arr.copy(), pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4]], 'Wrong answer'

    arr = [2436, 3283, 3084, 7906, 7143, 7333, 4150, 2398, 9745, 8529]
    pivot_index = 4
    print(arr[pivot_index])
    print(partition(arr.copy(), pivot_index))
    print(partition2(arr.copy(), pivot_index))