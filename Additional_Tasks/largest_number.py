# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.

from functools import cmp_to_key


def largestNumber(nums: list[int]) -> str:
    sorted_nums = sorted(
        map(str, nums),
        key=cmp_to_key(lambda a, b: 1 if a + b > b + a else -1),
        reverse=True
    )
    string_ans = "".join(sorted_nums)
    return str(int(string_ans))


nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))
