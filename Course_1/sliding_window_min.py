# Given an array aa, a sliding window of size kk  is moving from the very
# left of the array to the very right. Each time the sliding window moves
# right by one position. For each sliding window position return minimum
# value of all numbers inside the sliding window.
#
# Implement a function sliding_window_min(a, k) which returns a list of
# minimums for each sliding window position.
#
# Input data:
# List a integers, len(a)≤150000, k≤1000.
# Output data:
# The function has to return a list of integers.
#
# Example:
# Input: a = [1, 3, 4, 5, 2, 7], k = 3
# Output: [1, 3, 2, 2]
#
# To satisfy time limit for this task your solution has to work for O(n).
# To find hints how to achieve this time complexity estimation watch again screencast
# about queue implementation and think about how to use queue for this task and how to
# extract minimum from queue for O(1).


class Deque:

    def __init__(self):
        self.queue = []

    def push_front(self, key):
        self.queue.insert(0, key)

    def push_back(self, key):
        self.queue.append(key)

    def pop_front(self):
        if self.queue:
            return self.queue.pop(0)

    def pop_back(self):
        if self.queue:
            return self.queue.pop()

    def front(self):
        if self.queue:
            return self.queue[0]

    def back(self):
        if self.queue:
            return self.queue[-1]

    def clear(self):
        self.queue = []

    def size(self):
        return len(self.queue)


def sliding_window_min(a, k):
    if len(a) == 0 or k == 0:
        return
    elif len(a) <= k:
        return [min(a)]
    else:
        d = Deque()
        result = []
        for i in range(0, k):
            while d.size() > 0 and a[d.back()] >= a[i]:
                d.pop_back()
            d.push_back(i)
        result.append(a[d.front()])
        for i in range(k, len(a)):
            while d.size() > 0 and i - k >= d.front():
                d.pop_front()
            while d.size() > 0 and a[d.back()] >= a[i]:
                d.pop_back()
            d.push_back(i)
            result.append(a[d.front()])
    return result


# some test code
if __name__ == "__main__":
    test_a, test_k = [1, 3, 4, 5, 2, 7], 3
    # should print [1, 3, 2, 2]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [5, 4, 10, 1], 2
    # should print [4, 4, 1]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [10, 20, 6, 10, 8], 5
    # should print [6]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [0, 2, 2], 1
    # should print [0, 2, 2]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [1, 3, 1, 2, 4], 4
    # should print [1, 1]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [0, 11, 9, 7, 9, 1, 1, 2, 10], 8
    # should print [0, 1]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [9, 4, 9, 7, 8, 3, 5, 5, 7, 6, 11, 8], 3
    # should print [4, 4, 7, 3, 3, 3, 5, 5, 6, 6]
    print(sliding_window_min(test_a, test_k))

    import random

    flag = False
    while flag:
        a = []
        result = []
        for i in range(0, random.randint(5, 15)):
            n = random.randint(0, 11)
            a.append(n)
        k = random.randint(1, i+2)
        if k >= len(a):
            result.append(min(a))
        elif k == 0:
            pass
        else:
            for i in range(len(a) - k + 1):
                result.append(min(a[i: i + k]))
        print(result)
        test_a, test_k = a, k
        try:
            assert result == sliding_window_min(test_a, test_k)
            print("ok")
        except:
            print("fail", test_a, test_k, result, sliding_window_min(test_a, test_k))
            flag = False
