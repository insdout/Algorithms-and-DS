from random import randint


def bs(A, t, l=0, r=None):
    r = len(A) if r is None else r
    #print(l, r)
    if l >= r:
        return None
    mid = (l + r) // 2
    if A[mid] == t:
        return mid
    if A[mid] > t:
        return bs(A, t, l, mid)
    return bs(A, t, mid + 1, r)


def bsearch1(arr, key):
    low, high = 0, len(arr)
    while high - low > 1:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid
        else:
            high = mid
    return None


def bsearch1e(arr, key):
    low, high = 0, len(arr)
    while high - low >= 1:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid
    return None

def bsearch2(arr, key, left=0, right=None):
    if right is None:
        right = len(arr)
    if right < left:
        return None
    middle = (left + right) >> 1
    if arr[middle] > key:
        return bsearch2(arr, key, left, middle)
    if arr[middle] < key:
        return bsearch2(arr, key, middle + 1, right)
    return middle


def bsearch2e(arr, key, left=0, right=None):
    if right is None:
        right = len(arr)
    if right <= left:
        return None
    middle = (left + right) >> 1
    if arr[middle] > key:
        return bsearch2e(arr, key, left, middle)
    if arr[middle] < key:
        return bsearch2e(arr, key, middle + 1, right)
    return middle

def bsearch3(arr, key):
    n = len(arr)
    if n < 2:
        return (0 if (n == 1 and arr[0] == key) else None)
    m = int(0.5 * n)
    if arr[m] > key:
        return bsearch3(arr[:m], key)
    result = bsearch3(arr[m:], key)
    return (result + m if result != None else None)


def bsearch3e(arr, key, left=0, right=None):
    right = len(arr) if right is None else right
    n = right + left
    if left >= right:
        return None

    m = int(0.5 * n)
    if arr[m] > key:
        return bsearch3e(arr, key, left, m)
    elif arr[m] < key:
        return bsearch3e(arr, key, m + 1, right)
    return m

def generate_test(max_len, max_int):
    case_len = randint(0, max_len)
    case = [sorted([randint(0, max_int) for _ in range(case_len)]), randint(0, max_int + max_int//2)]
    return case


def test_bs(test_case, correct_algorithm, alg_to_test):
    flag = True
    answer = correct_algorithm(*test_case)
    for alg in alg_to_test:
        if alg(*test_case) != answer:
            if test_case[0][alg(*test_case)] == test_case[1]:
                print(alg.__name__, alg(*test_case), ":Ok", answer)
            else:
                print(test_case, alg.__name__, "Wrong:", alg(*test_case), "Expected:", answer)
                flag = False
        else:
            print(alg.__name__, alg(*test_case), ":Ok", answer)
    return flag


if __name__ == "__main__":

    print(bsearch3e([1, 3, 4, 6, 6], 6))

    test_cases = [
        [[], 1],
        [[1], 1],
        [[1], 2],
        [[1, 2], 3],
        [[1, 2], 1],
        [[1, 2], 2],
        [[1, 2, 3], 1],
        [[1, 2, 3], 2],
        [[1, 2, 3], 3],
        [[1, 2, 3], 4],
        [[1, 2, 3, 4], 1],
        [[1, 2, 3, 4], 4],
        [[1, 2, 3, 4], 2],
        [[1, 2, 3, 4], 5]
    ]

    for test_case in test_cases:
        print(test_case)
        test_bs(test_case, bs, [bsearch1e, bsearch2e, bsearch3])

    flag = True
    iterations = 0
    while flag and iterations < 20:
        case = generate_test(20, 10)
        print(case)
        flag = test_bs(case, bs, [bsearch1e, bsearch2e, bsearch3e])
        iterations += 1
