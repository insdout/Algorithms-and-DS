from random import randint


def partition(a, left, right):
    pivot = left
    while left < right:
        while a[left] <= a[pivot] and left < len(a)-1:
            left += 1
        while a[right] > a[pivot] and right > 0: #why not >=?
            right -= 1
        if left < right:
            a[left], a[right] = a[right], a[left]
    a[pivot], a[right] = a[right], a[pivot]
    return right


def quick_sort(a, left, right):
    if left < right:
        pivot = partition(a, left, right)
        quick_sort(a, left, pivot-1)
        quick_sort(a, pivot+1, right)


def generate_list(length):
    return [randint(0, 20) for i in range(length)]


def test_unit(length):
    case = generate_list(length)
    print("Test Case:", case)
    a = case.copy()
    answer = sorted(a.copy())
    quick_sort(a, 0, len(a) - 1)
    err_string = "Failed case: {1}, answer: {2}, correct answer: {3}"
    assert a == answer, err_string.format(case,a, answer)


def run_tests(length, repetitions):
    for i in range(length):
        for j in range(repetitions):
            test_unit(i)
    print("Test Passed!")

if __name__ == "__main__":
    a = [10, 7, 8, 9, 1, 5]
    a = [4, 9, 14]
    quick_sort(a, 0, len(a)-1)
    print(a)
    print("RUN TESTS:")
    run_tests(10, 20)
