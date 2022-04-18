# Given a Minimum Binary Heap implement a sift_down method.

class MinHeap:
    def __init__(self):
        self._heap = []

    def pop(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        elem = self._heap.pop()
        self._sift_down(0)

    def _sift_down(self, index):
        n = len(self._heap)
        while (2*index + 1) < n:
            smallest = index
            left = 2*index + 1
            right = 2*index + 2
            if left < n and self._heap[smallest] > self._heap[left]:
                smallest = left
            if right < n and self._heap[smallest] > self._heap[right]:
                smallest = right
            if index != smallest:
                self._heap[smallest], self._heap[index] = self._heap[index], self._heap[smallest]
                index = smallest
            else:
                break


if __name__ == "__main__":
    heap = MinHeap()
    heap._heap = [1, 2, 3]
    heap.pop()

    # check that your code works correctly on provided example
    assert heap._heap == [2, 3], 'Wrong answer'