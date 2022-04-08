# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
#
# Example 1:
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
#
# Example 2:
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
#
# Constraints:
# 1 <= nums.length <= 2*10^5
# 0 <= nums[i] <= 2^31 - 1
#
# Runtime: 7133 ms, faster than 16.25% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
# Memory Usage: 144.3 MB, less than 12.88% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.

class Trie_Node:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Trie_Node()
        self.opposite = {"1": "0", "0": "1"}

    def insert(self, number :int):
        bin_number = bin(number)[2:].zfill(32)
        node = self.root
        for digit in bin_number:
            if digit in node.children:
                node = node.children[digit]
            else:
                new_node = Trie_Node()
                node.children[digit] = new_node
                node = new_node

    def max_xor(self, number: int):
        bin_number = bin(number)[2:].zfill(32)
        node = self.root
        max_xor_val = ""
        for digit in bin_number:
            op_digit = self.opposite[digit]
            if op_digit in node.children:
                max_xor_val += op_digit
                node = node.children[op_digit]
            else:
                max_xor_val += digit
                node = node.children[digit]
        return int(max_xor_val, 2) ^ number


def findMaximumXOR(nums: list[int]) -> int:
    max_xor_val = 0
    t = Trie()
    for num in nums:
        t.insert(num)
    for num in nums:
        max_xor_val = max(max_xor_val, t.max_xor(num))
    return max_xor_val


if __name__ == "__main__":
    nums = [3, 10, 5, 25, 2, 8]
    assert findMaximumXOR(nums) == 28, "Wrong Answer"
