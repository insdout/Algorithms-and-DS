# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
#
# Example 1:
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
#
# Example 2:
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
#
# Runtime: 5647 ms, faster than 40.16% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 40.1 MB, less than 11.77% of Python3 online submissions for Maximum Length of Repeated Subarray.

def findLength(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    m = len(nums2)
    max_len = 0
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if nums1[i-1] == nums2[j-1]:
                d[i][j] = d[i-1][j-1] + 1
                if d[i][j] > max_len:
                    max_len = d[i][j]
            else:
                d[i][j] = 0
    print(*d, sep="\n")
    return max_len


if __name__ == "__main__":
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    print(findLength(nums1, nums2))