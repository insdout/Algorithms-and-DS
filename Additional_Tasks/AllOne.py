# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.
#
# Implement the AllOne class:
#
# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1.
# If key does not exist in the data structure, insert it with count 1.

# dec(String key) Decrements the count of the string key by 1.
# If the count of key is 0 after the decrement, remove it from the data structure.
# It is guaranteed that key exists in the data structure before the decrement.

# getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
#
#
# Example 1:
#
# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]
#
# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"
import heapq
class AllOne:

    def __init__(self):
        self.d = {}
        self.minheap = []
        self.maxheap = []

    def inc(self, key: str) -> None:
        self.d[key] = self.d.get(key, 0) + 1
        heapq.heappush((self.d[key], key))

    def dec(self, key: str) -> None:
        self.d[key] -= 1
        if self.d[key] <= 0:
            del self.d[key]


    def getMaxKey(self) -> str:


    def getMinKey(self) -> str:


if __name__ == "__main__":
    # Your AllOne object will be instantiated and called as such:

    allOne = AllOne()
    allOne.inc("hello")
    allOne.inc("hello")
    allOne.getMaxKey() # return "hello"
    allOne.getMinKey() # return "hello"
    allOne.inc("leet")
    allOne.getMaxKey() # return "hello"
    allOne.getMinKey() # return "leet"