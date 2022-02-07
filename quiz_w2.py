class Queue:

    def __init__(self, max_len=100):
        self.max_len = max_len + 1
        self.queue = [0] * self.max_len
        self.head = 0
        self.tail = 0

    def empty(self):
        return self.head == self.tail

    def enqueue(self, key):
        self.queue[self.tail] = key
        self.tail = (self.tail + 1) % self.max_len

    def dequeue(self):
        if not self.head == self.tail:
            res = self.queue[self.head]
            self.head = (self.head + 1) % self.max_len
            return res
        else:
            return "error"

if __name__ == "__main__":
    q = Queue(2)
    print(q.dequeue())
    print(q.enqueue(1))
    print(q.dequeue())
