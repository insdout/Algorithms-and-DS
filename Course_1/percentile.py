from math import ceil
from random import randint


def kth_element(a, b, k, pointer_a=0, pointer_b=0):
    if pointer_a == len(a):
        return b[pointer_b + k - 1]
    if pointer_b == len(b):
        return a[pointer_a + k - 1]
    if k == 1:
        return min(a[pointer_a], b[pointer_b])
    mid = k//2

    if mid > len(a) - pointer_a:
        if a[-1] < b[pointer_b + mid - 1]:
            return b[pointer_b + k - len(a) + pointer_a - 1]
        else:
            return kth_element(a, b, k - mid, pointer_a, pointer_b + mid)
    elif mid > len(b) - pointer_b:
        if b[-1] < a[pointer_a + mid - 1]:
            return a[pointer_a + k - len(b) + pointer_b - 1]
        else:
            return kth_element(a, b, k - mid, pointer_a + mid, pointer_b)
    else:
        if a[pointer_a + mid - 1] > b[pointer_b + mid - 1]:
            return kth_element(a, b, k - mid, pointer_a, pointer_b + mid)
        else:
            return kth_element(a, b, k - mid, pointer_a + mid, pointer_b)


def find_percentile(a, b, p):
    k = ceil((len(a) + len(b))*p/100)
    return kth_element(a, b, k)


def find_percentile_reference(a, b, p):
    k = ceil((len(a) + len(b))*p/100)
    pointer_a = 0
    pointer_b = 0
    result = -1
    while pointer_a < len(a) and pointer_b < len(b) and k > 0:
        if a[pointer_a] <= b[pointer_b]:
            result = a[pointer_a]
            k -= 1
            pointer_a += 1
        else:
            result = b[pointer_b]
            k -= 1
            pointer_b += 1
    while pointer_a < len(a) and k > 0:
        result = a[pointer_a]
        k -= 1
        pointer_a += 1
    while pointer_b < len(b) and k > 0:
        result = b[pointer_b]
        k -= 1
        pointer_b += 1
    return result


def test_percentile(test_case, correct_answer):
    answer = find_percentile(*test_case)
    error_string = "FAILED! Input: {0}\nOutput: {1}\nCorrect Output: {2}"
    assert answer == correct_answer, \
        error_string.format(test_case, answer, correct_answer)


def run_test():
    test_percentile([[1], [], 10], 1)
    test_percentile([[1], [], 80], 1)
    test_percentile([[1, 2], [], 10], 1)
    test_percentile([[1, 2], [], 80], 2)
    test_percentile([[], [1, 2], 10], 1)
    test_percentile([[], [1, 2], 80], 2)
    test_percentile([[1, 2], [3, 4], 100], 4)
    test_percentile([[1, 2], [3, 4], 50], 2)
    test_percentile([[1, 2, 7, 8, 10], [6, 12], 50], 7)
    test_percentile([[1, 2, 7, 8], [6, 12], 50], 6)
    test_percentile([[15, 20, 35, 40, 50], [], 30], 20)
    test_percentile([[15, 20], [25, 40, 50], 40], 20)
    test_percentile([[1, 99], [15, 16, 18, 20], 100], 99)
    print("Unit test passed!")


def generate_random_test(a_length, b_length, int_range_left, int_range_right, p):
    a = sorted([randint(int_range_left, int_range_right) for _ in range(a_length)])
    b = sorted([randint(int_range_left, int_range_right) for _ in range(b_length)])
    return [a, b, p]


def run_stress_test(max_len, int_range, max_attempts):
    for i in range(max_len):
        if i % 10 == 0:
            print(i, "out of", max_len, "done.")
        for j in range(max_len):
            if i == j == 0:
                pass
            else:
                for p in range(10, 110, 10):
                    for _ in range(max_attempts):
                        random_test = generate_random_test(i, j, 0, int_range, p)
                        answer = find_percentile_reference(*random_test)
                        test_percentile(random_test, answer)
    print("Stress test passed!")


def run_max_test(max_attempts, max_len=10**6, int_range=100):
    for i in range(max_attempts):
        if i % 5 == 0:
            print(i, "out of", max_attempts, "done.")
            for p in [1, 100]:
                random_test = generate_random_test(max_len, max_len, int_range, int_range, p)
                answer = find_percentile_reference(*random_test)
                test_percentile(random_test, answer)
    print("Max test passed!")


# some test code
if __name__ == "__main__":
    run_test()
    #Arguments: max_len, int_range, max_attempts
    run_stress_test(50, 10, 10)
    # Arguments: max_attempts, max_len=10**6, int_range=100
    run_max_test(10)

