from math import ceil


def kth_element(arr1, arr2, k, p1=0, p2=0):
    if p1 == len(arr1):
        return arr2[p2 + k - 1]
    if p2 == len(arr2):
        return arr1[p1 + k - 1]
    if k == 0 or k > (len(arr1) - p1) + (len(arr2) - p2):
        return -1
    if k == 1:
        return min(arr1[p1], arr2[p2])
    mid = k//2

    if mid > len(arr1) - p1:
        if arr1[-1] < arr2[p2 + mid - 1]:
            return arr2[p2 + k - len(arr1) + p1 - 1]
        else:
            return kth_element(arr1, arr2, k-mid, p1, p2 + mid)

    if mid > len(arr2) - p2:
        if arr2[-1] < arr1[p1 + mid - 1]:
            return arr1[p1 + k - len(arr2) + p2 - 1]
        else:
            return kth_element(arr1, arr2, k-mid, p1+mid, p2)
    else:
        if arr1[p1+mid-1] > arr2[p2+mid-1]:
            return kth_element(arr1, arr2, k-mid, p1, p2+mid)
        else:
            return kth_element(arr1, arr2, k-mid, p1+mid, p2)


def find_percentile(a, b, p):
    k = ceil((len(a) + len(b))*p/100)
    return kth_element(a, b, k)

# some test code
if __name__ == "__main__":

    test_a, test_b, test_p = [1, 99], [15, 16,18,20], 100
    # should print 20
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    # should print 7
    print(find_percentile(test_a, test_b, test_p))


    test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    # should print 6
    print(find_percentile(test_a, test_b, test_p))


    test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    # should print 20
    print(find_percentile(test_a, test_b, test_p))


    test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    # should print 20
    print(find_percentile(test_a, test_b, test_p))


    test_a, test_b, test_p = [15,15, 15], [15], 99
    # should print 20
    print(find_percentile(test_a, test_b, test_p))


    test_a, test_b, test_p = [1,99],[15, 16,17,18,19,20], 100
    # should print 20
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [1, 99], [15, 16,18,20], 100
    # should print 20
    print(find_percentile(test_a, test_b, test_p))
