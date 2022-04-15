# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.


def largestNumber(nums: list[int]) -> str:
    print(sorted(map(str, nums)))




nums = [3,30,34,5,9]
print(largestNumber(nums))
