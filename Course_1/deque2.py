# Deque (double-ended queue) is an abstract data structure with the following operation
#
# -push_front adds a key to the head of the deque
# -push_back adds a key to the tail of the deque
# -pop_front extracts a key from the head of the deque and returns it
# -pop_back extracts a key from the tail of the deque and returns it
# -front returns head element without removing it
# -back returns tail element without removing it
# -size returns number of the elements in the deque
# -clear removes all elements from the deque
#
# Implement DequeDeque class with this methods and error handling.
# For pop_front, pop_back, front, back
# the method has to check are there elements in the deque.
# If it is empty the method has to return string "error" instead of a numeric value.
#
# push_front, push_back, clear methods has to return string "ok".
#
# Implement process_deque(commands) which takes commands list and returns a list of answers to each command.
#
# Input data:
# List commands consisting of strings "push_front x", "push_back x", "pop_front",
# "pop_back", "front", "back", "size", "clear".
#
# len(commands)≤60000
#
# Output data:
# A list of answers for each command
# Example:
#
# Input: Input:
#
#commands=["push_front 1","push_front 2","push_back 6","front","back","clear","size","back"]
# Output: ["ok", "ok", "ok",  2, 6, "ok", 0, "error"]


class Deque:

    def __init__(self, max_len=10):
        self.max_length = max_len + 2
        self.queue = [0] * self.max_length
        self.head = 0
        self.tail = 0

    def full(self):
        if (self.tail + 1) % self.max_length == self.head:
            print("Full", self.tail, self.head)
            return True
        else:
            return False

    def empty(self):
        return self.head == self.tail

    def push_front(self, key):
        if not self.full():
            self.queue[self.head] = key
            self.tail = (self.tail + 1) % self.max_length if self.empty() else self.tail
            self.head = (self.head - 1) % self.max_length
            return "ok"

    def push_back(self, key):
        if not self.full():
            self.queue[self.tail] = key
            self.head = (self.head - 1) % self.max_length if self.empty() else self.head
            self.tail = (self.tail + 1) % self.max_length
            return "ok"

    def pop_front(self):
        if not self.empty():
            self.head = (self.head + 1) % self.max_length
            res = self.queue[self.head]
            return res
        else:
            return "error"

    def pop_back(self):
        if not self.empty():
            self.tail = (self.tail - 1) % self.max_length
            res = self.queue[self.tail]
            return res
        else:
            return "error"

    def front(self):
        if not self.empty():
            return self.queue[(self.head + 1)% self.max_length]
        else:
            return "error"

    def back(self):
        if not self.empty():
            return self.queue[(self.tail - 1)% self.max_length]
        else:
            return "error"

    def clear(self):
        self.head = self.tail = 0
        return "ok"

    def size(self):
        if self.empty():
            return 0
        else:
            return (self.tail - self.head) % self.max_length - 1


def process_deque(commands):
    d = Deque()
    results = []
    for command in commands:
        command_split = command.split()
        method_name = command_split[0]
        arg = command_split[1] if len(command_split) == 2 else None
        method = getattr(d, method_name)
        if arg is not None:
            results.append(method(int(arg)))
        else:
            results.append(method())
    return results




if __name__ == "__main__":
    test_cmd = ["push_front 1", "push_front 2", "push_back 6", "front", "back", "clear", "size", "back"]
    # should print ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
    print(process_deque(test_cmd))

    test_cmd = ["pop_front", "back", "push_back 2", "size"]
    # should print ["error", "error", "ok", 1]
    print(process_deque(test_cmd))

    test_cmd = ["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))

    test_cmd = ["push_back 1", "size","push_back 2", "size","push_back 3", "push_back 4", "push_back 5",
                "push_back 6", "push_back 7", "push_back 8", "push_back 9","size", "push_back 10", "size",
                "pop_front","push_back 11","size","back","front","push_back 12"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))