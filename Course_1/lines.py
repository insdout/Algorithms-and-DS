# In lines computer game, a player sets balls of different colors in a line.
# When a continuous block of three or more balls of the same color is formed,
# it is removed from the line. In this case, all the balls are shifted to each other,
# and the situation may be repeated.
# Write a function lines(a) that determines how many balls will be destroyed.
# There can be at most one continuous block of three or more same-colored balls
# at the initial moment.
#
# Input data:
# The function takes a list aa with initial balls disposition. Balls number is
# less or equals 1000, balls colors can be from 0 to 9, each color has its own integer.
#
# Output data:
# The function has to return one number, the number of the balls that will be destroyed.
#
# Example:
# Input: [2, 2, 1, 1, 1, 2, 1]
# Output: 6
#
# Comment:
# After three balls color of 1 were destroyed, balls shifted to the left
# and new disposition [2, 2, 2, 1] appears. Three balls color of 2 were destroyed too.


def print_a(a, left, right):
    print(*a)
    string = [" " for i in range(len(a))]
    string[left] = "^"
    string[right] = "^"
    print(*string)


def lines(a):
    left = 0
    right = 0
    destroyed = 0
    skipped = 0
    while right < len(a):
        if a[right] != a[left]:
            if right - left - destroyed >= 3:
                destroyed += right - left - destroyed
                skipped += destroyed
                if a[left-1] == a[right] and left > 0:
                    while a[left-1] == a[right] and left > 0:
                        left -= 1

                    if right < len(a) - 1:
                        while right < len(a)-1:
                            if a[right + 1] == a[right]:
                                right += 1
                            else:
                                break
                    if right - left - destroyed < 2:
                        left = right
                        skipped = 0
                else:
                    left = right
                right += 1

            else:
                left += 1
                right += 1

        else:
            right += 1
    if right - left - skipped >= 3:
        destroyed += right - left - skipped
    return destroyed


# some test code
if __name__ == "__main__":
    test_a = [2, 2, 1, 1, 1, 2, 1]
    # should print 6
    print(lines(test_a))

    test_a = [0, 0, 0, 0, 0]
    # should print 5
    print(lines(test_a))

    test_a = [2, 3, 1, 4]
    # should print 0
    print(lines(test_a))

    test_a = [4, 4, 2, 2, 1, 1, 1, 2, 4, 1]
    # should print 9
    print(lines(test_a))

    test_a = [4, 2, 1, 1, 1, 2, 4, 5, 6, 7, 1, 1, 1, 1]
    # should print 7
    print(lines(test_a))

    test_a = [7, 1, 1, 1, 7, 7]
    # should print 6
    print(lines(test_a))

    test_a = [1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1]
    # should print 3
    print(lines(test_a))
