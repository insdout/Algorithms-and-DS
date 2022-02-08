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

    def __init__(self):
        self.queue = []

    def push_front(self, key):
        self.queue.insert(0, key)
        return "ok"

    def push_back(self, key):
        self.queue.append(key)
        return "ok"

    def pop_front(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return "error"

    def pop_back(self):
        if self.queue:
            return self.queue.pop()
        else:
            return "error"

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return "error"

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return "error"

    def clear(self):
        self.queue = []
        return "ok"

    def size(self):
        return len(self.queue)


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