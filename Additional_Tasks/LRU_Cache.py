# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
#
#
#
# Example 1:
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete_node(self, node):
        if self.head == node:
            self.pop_oldest()
            return
        if self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            return

        node_p = node.prev
        node_n = node.next
        node_p.next = node_n
        node_n.prev = node_p

    def rise_on_top(self, node):
        if self.tail == node:
            return
        if self.head == node:
            self.pop_oldest()
            self.append(node)
            return
        self.delete_node(node)
        self.append(node)


    def pop_oldest(self):
        if not self.head:
            return
        if self.head != self.tail:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None

    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            tmp = self.tail
            node.prev = tmp
            tmp.next = node
            self.tail = node
            self.tail.next = None

    def __repr__(self):
        list = []
        node = self.head
        emergency = 100
        while node and emergency:
            list.append({node.key:node.val})
            node = node.next
            #print("appending", list)
            emergency -= 1
        return str(list) +" -> Tail: "+ str(self.tail.val)


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = DLList()
        self.capacity = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            value = self.d[key].val
            self.cache.rise_on_top(self.d[key])
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.cache.rise_on_top(self.d[key])
        else:
            if self.capacity <= 0:
                key_to_remove = self.cache.head.key
                self.cache.pop_oldest()
                del self.d[key_to_remove]
                self.capacity += 1
            node = ListNode(key, value)
            self.d[key] = node
            self.cache.append(node)
            self.capacity -= 1
        print(self.cache)


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)      # cache is {1 = 1}
    lRUCache.put(2, 2)      # cache is {1 = 1, 2 = 2}
    print(lRUCache.get(1))  # return 1
    lRUCache.put(3, 3)      # LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
    print(lRUCache.get(2))  # returns - 1(not found)
    lRUCache.put(4, 4)      # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
    print(lRUCache.get(1))  # return -1(not found)
    print(lRUCache.get(3))  # return 3
    print(lRUCache.get(4))  # return 4

    lRUCache.put(4, 5)
    lRUCache.put(3, 33)
    lRUCache.put(5, 55)
    lRUCache.put(1, 11)