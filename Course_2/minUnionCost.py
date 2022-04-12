# You are given several sets and a following operation: you can unite two sets into one set with the size equal
# to the sum of the sizes of the two original sets. the cost of this operation is the size of the resulting set.
# Find a way to unite all the sets into one, with the total sum of all operations used to do this minimal.


import heapq


def minUnionCost(set_sizes):
    n = len(set_sizes)
    min_sum = 0
    heap = set_sizes.copy()
    heapq.heapify(heap)
    while len(heap) > 2:
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        heapq.heappush(heap, min1 + min2)
        min_sum += min1 + min2
    min_sum += sum(heap)
    return min_sum


if __name__ == "__main__":
    set_sizes = [2, 6]
    # check that your code works correctly on provided example
    assert minUnionCost(set_sizes) == 8, 'Wrong answer'

    set_sizes = [5, 5, 1, 1]
    # check that your code works correctly on provided example
    assert minUnionCost(set_sizes) == 21, 'Wrong answer'

    set_sizes = [2, 6, 8, 9, 14]
    # check that your code works correctly on provided example
    assert minUnionCost(set_sizes) == 86, 'Wrong answer'

    set_sizes = []
    # check that your code works correctly on provided example
    assert minUnionCost(set_sizes) == 0, 'Wrong answer'