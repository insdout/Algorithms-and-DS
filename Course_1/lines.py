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

    test_a = [4, 2, 1, 1, 1, 2, 4,5,6,7, 1, 1, 1,1]
    # should print 7
    print(lines(test_a))

    test_a = [ 7, 1, 1, 1,7,7]
    # should print 6
    print(lines(test_a))

    test_a = [1,1,2,1,2,2,1,1,1,2,1,1]
    # should print 3
    print(lines(test_a))

