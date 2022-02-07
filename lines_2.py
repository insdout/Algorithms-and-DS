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
    while right < len(a):
        print_a(a, left, right)
        if a[left] != a[right]:
            if right - left > 2:
                destroyed += right - left
                del a[left:right]
                right -= right - left
                left -= 1

                #print("destr",destroyed)
                while a[right] == a[left] and left > 0:
                    if a[left-1] == a[right]:
                        left -= 1
                    else:
                        break
            else:
                left = right
                right += 1
        else:
            right += 1
    if right - left > 2:
        destroyed += right - left

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
    # should print 9
    print(lines(test_a))