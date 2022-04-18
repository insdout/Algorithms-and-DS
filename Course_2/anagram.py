# Question 1
#
# Given two strings determine if one of them is an anagram of the other.

def isAnagram(string1, string2):
    is_anagram = True
    d = {}
    if len(string1) != len(string2):
        return False
    for char in string1:
        d[char] = d.get(char, 0) + 1
    for char in string2:
        if char not in d:
            return False
        else:
            d[char] = d[char] - 1
            if d[char] < 0:
                return False

    return is_anagram

# Question 2
#
# Given a string find the lengths of its longest substring without repeating characters.

def longestNonRepeating(text):
    n = len(text)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    longest = 0
    d = {}
    left = 0
    for i in range(n):
        char = text[i]
        right = i
        if char in d:
            temp = d.get(char)
            left = max(left, temp + 1)
        longest = max(longest, right - left + 1)
        d[char] = i
    return longest


def arrayIntersection(array1, array2):
    intersection = []
    s1 = set(array1)
    s2 = set(array2)
    intersection.extend(list(s1.intersection(s2)))

    return intersection

if __name__ == "__main__":
    string1 = 'baa'
    string2 = 'aab'
    # check that your code works correctly on provided example
    assert isAnagram(string1, string2), 'Wrong answer'

    string1 = 'baa'
    string2 = 'acb'
    # check that your code works correctly on provided example
    assert not isAnagram(string1, string2), 'Wrong answer'

    string1 = 'baa'
    string2 = 'aaab'
    # check that your code works correctly on provided example
    assert not isAnagram(string1, string2), 'Wrong answer'

    string1 = "coronavirus"
    string2 = "carnivorous"
    # check that your code works correctly on provided example
    assert isAnagram(string1, string2), 'Wrong answer'

    text = '12121212'
    # check that your code works correctly on provided example
    assert longestNonRepeating(text) == 2, 'Wrong answer'

    array1 = [1, 2, 3]
    array2 = [2, 4, 5]
    # check that your code works correctly on provided example
    assert arrayIntersection(array1, array2) == [2], 'Wrong answer'

    array1 = [1, 2, 3]
    array2 = [6, 4, 5]
    # check that your code works correctly on provided example
    assert arrayIntersection(array1, array2) == [], 'Wrong answer'

    array1 = [1, 2, 3]
    array2 = [1, 2, 4, 5]
    # check that your code works correctly on provided example
    assert arrayIntersection(array1, array2) == [1, 2], 'Wrong answer'