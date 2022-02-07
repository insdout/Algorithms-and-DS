def largest_palindrome(s):
    centers = []
    w = 1
    for i in range(1, len(s)-1):
        if s[i-w] == s[i+w]:
            centers.append(i)
    if len(centers) == 0:
        return s[0]
    else:
        while len(centers) > 0:
            w += 1
            del_c = []
            for c in centers:
                if c+w < len(s) and c-w >= 0:
                    if s[c-w] == s[c+w]:
                        pass
                    else:
                        del_c.append(c)
                        centers.remove(c)
                else:
                    del_c.append(c)
                    centers.remove(c)
        return s[del_c[0]-w+1:del_c[0]+w]




# some test code
if __name__ == "__main__":
    test_s = 'BAA'
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

