# Design your implementation of the circular queue. The circular queue is a linear data structure
# in which the operations are performed based on FIFO (First In First Out) principle
# and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".
#
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
# In a normal queue, once the queue becomes full, we cannot insert the next element even if
# there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
#
# Implementation the MyCircularQueue class:
#
# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language.


class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next =next
        self.prev = prev

class DLList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_right(self, node):
        n_prev, n_next = self.tail.prev, self.tail
        node.prev, node.next = n_prev, n_next
        n_prev.next , n_next.prev = node, node
        self.size += 1

    def popleft(self):
        print("before_pop", self)
        n_prev, n_next = self.head, self.head.next
        if n_next != self.tail:
            n_next = n_next.next
            n_next.prev, n_prev.next = n_prev, n_next
            self.size -= 1
            print("after_pop", self)
            return True
        else:
            print("no_pop", self)
            return False

    def __repr__(self):
        list = []
        node = self.head
        emergency = 100
        while node and emergency:
            list.append(node.val)
            node = node.next
            #print("appending", list)
            emergency -= 1
        return str(list) +" -> Tail.prev: "+ str(self.tail.prev.val)

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = DLList()

    def enQueue(self, value: int) -> bool:
        if self.queue.size < self.size:
            node = Node(value)
            self.queue.add_right(node)
            print(self.queue)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        return self.queue.popleft()

    def Front(self) -> int:
        if self.queue.size > 0:
            return self.queue.head.next.val
        else:
            return -1

    def Rear(self) -> int:
        if self.queue.size > 0:
            return self.queue.tail.prev.val
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.queue.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.queue.size == self.size:
            return True
        else:
            return False


if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(3)
    print(myCircularQueue.enQueue(1)) # return True
    print(myCircularQueue.enQueue(2)) # return True
    print(myCircularQueue.enQueue(3)) # return True
    print(myCircularQueue.enQueue(4)) # return False
    print(myCircularQueue.Rear()) # return 3
    print(myCircularQueue.isFull()) # return True
    print(myCircularQueue.deQueue()) # return True
    print(myCircularQueue.enQueue(4)) # return True
    print(myCircularQueue.Rear()) # return 4

    print(myCircularQueue.deQueue())  # return True
    print(myCircularQueue.deQueue())  # return True
    print(myCircularQueue.deQueue())  # return True
    print(myCircularQueue.deQueue())  # return True