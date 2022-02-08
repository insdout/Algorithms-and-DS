# Given a string ss. Write a function largest_palindrome(s) that finds
# palindrome substring in ss with the maximum possible length.
#
# Input data:
#
# String ss containing upper-case english letters, len(s)≤1000.
#
# Output data:
# The function has to return a string which is the largest palindrome
# substring of ss. If there are several possible answers choose the
# closest one to the beginning of the string.
#
# Example:
# Input: ABBCB
# Output: BCB
#
# Part 1 tests will pass solutions working for O(n^3)
#To pass Part 2 tests the solution should work for O(n^2)
#To achieve this time complexity estimation try to fix palindrome center
# and to build a palindrome around it while it is possible.

def largest_palindrome(s):
    max_length = 1
    start = 0

    for i in range(1, len(s)):
        left = i-1
        right = i

        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1

        if s[left] == s[right] and right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
        left = i - 1
        right = i + 1
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1
        if s[left] == s[right] and right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
    return s[start:start+max_length]





# some test code
if __name__ == "__main__":
    test_s = 'BcdAgAAAA'
    # should print BCB
    print(largest_palindrome(test_s))

    test_s = '1232345654367'
    # should print BCB
    print(largest_palindrome(test_s))

    test_s = 'ABBCB'
    # should print BCB
    print(largest_palindrome(test_s))

    test_s = 'ABACABAD'
    # should print ABACABA
    print(largest_palindrome(test_s))

    test_s = 'ABCDE'
    # should print A
    print(largest_palindrome(test_s))

