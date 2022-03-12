from random import randint


def max_heapify(a, i, n):
    max_i = i
    if 2*i+1 < n and a[max_i] < a[2*i+1]:
        max_i = 2*i+1
    if 2*i+2 < n and a[max_i] < a[2*i+2]:
        max_i = 2*i + 2
    if max_i != i:
        a[i], a[max_i] = a[max_i], a[i]
        max_heapify(a, max_i, n)


def build_max_heap(a, n):
    for i in range(n//2-1, -1, -1):
        max_heapify(a, i, n)


def heap_sort(a):
    build_max_heap(a, len(a))
    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, 0, i)
    return a


def generate_list(length):
    return [randint(0, 20) for i in range(length)]


def test_unit(length):
    case = generate_list(length)
    print("Test Case:", case)
    a = case.copy()
    answer = sorted(a.copy())
    heap_sort(a)
    err_string = "Failed case: {1}, answer: {2}, correct answer: {3}"
    assert a == answer, err_string.format(case,a, answer)


def run_tests(length, repetitions):
    for i in range(length):
        for j in range(repetitions):
            test_unit(i)
    print("Test Passed!")


if __name__ == "__main__":
    a = [16, 14, 10, 4, 7, 9, 3, 2, 8, 1]
    b = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

    print(heap_sort(b.copy()))
    build_max_heap(b, len(b))
    print(b)
    max_heapify(a, 3, len(a))
    print(a)
    print("RUN TESTS:")
    run_tests(10, 20)