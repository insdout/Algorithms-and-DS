# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: nums = [3,1,3,4,2]
# Output: 3

def findDuplicate(nums: list[int]) -> int:
    fast = nums[nums[0]]
    slow = nums[0]

    while fast != slow:
        fast = nums[nums[fast]]
        slow = nums[slow]
        print("f:", fast, "s:", slow)
    len_cycle = 1
    fast = nums[fast]
    print("cycle:", fast)
    while fast != slow:
        fast = nums[fast]
        print("cycle:", fast)
        len_cycle += 1
    print("len:", len_cycle)
    fast = nums[0]
    for _ in range(len_cycle-1):
        fast = nums[fast]
    print("fast_start:", fast)
    slow = nums[0]
    fast = nums[fast]
    print("find")
    while fast != slow:
        fast = nums[fast]
        slow = nums[slow]
        print("f:", fast, "s:", slow)

    return slow

if __name__ == "__main__":
    l = [1,3,4,2,2]
    print(findDuplicate(l))
    assert findDuplicate(l) == 2

    l = [3,1,3,4,2]
    print(findDuplicate(l))
    assert findDuplicate(l) == 3

    l = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    print(findDuplicate(l))
    assert findDuplicate(l) == 9