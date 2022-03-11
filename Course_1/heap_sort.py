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


a = [16, 14, 10, 4, 7, 9, 3, 2, 8, 1]
b = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

print(heap_sort(b.copy()))
build_max_heap(b, len(b))
print(b)
max_heapify(a, 3, len(a))
print(a)