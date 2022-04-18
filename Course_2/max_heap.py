# Given a Maximum Binary Heap data structure implement the sift_up method. The method shouldn't return anything.

class MaxHeap:
    def __init__(self):
        self._heap = []

    def push(self, elem):
        self._heap.append(elem)
        self._sift_up(len(self._heap) - 1)

    def _sift_up(self, index):
        print(self._heap)
        while index:
            parent = (index - 1) // 2
            if self._heap[parent] < self._heap[index]:
                self._heap[parent], self._heap[index] = self._heap[index], self._heap[parent]
                index = parent
            else:
                break
        print(self._heap)


# YOUR CODE GOES HERE


if __name__ == "__main__":
    heap = MaxHeap()
    heap.push(1)
    heap.push(2)
    heap.push(3)

    # check that your code works correctly on provided example
    assert heap._heap in [[3, 2, 1], [3, 1, 2]], 'Wrong answer'