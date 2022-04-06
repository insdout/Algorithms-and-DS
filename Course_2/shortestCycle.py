

def z_function(text):
    n = len(text)
    z_array = [0 for i in range(n)]
    left, right, relative_ind = 0, 0, 0
    for i in range(1, n):
        if i > right:
            left, right = i, i
            while right < n and text[right - left] == text[right]:
                right += 1
            z_array[i] = right - left
            right -= 1
        else:
            relative_ind = i - left
            if z_array[relative_ind] < right - i + 1:
                z_array[i] = z_array[relative_ind]
            else:
                left = i
                while right < n and text[right - left] == text[right]:
                    right += 1
                z_array[i] = right - left
                right -= 1
    return z_array


def shortestCycle(s):
    z_array = z_function(s)
    n = len(s)
    res = len(s)
    for i in range(n-1, n//2 - 1, -1):
        candidate = z_array[i]
        print(candidate + i, n, "i:", i, "z[i]:", candidate)
        if candidate != 0 and candidate + i == n:
            if n % candidate != 0:
                print("catch here")
                continue
            flag = True
            for j in range(candidate, n, candidate):
                print("j:", j, "n:", n)
                if z_array[j] < candidate:
                    print("break")
                    flag = False
                    break
                print("z", z_array[j], n)
            if flag:
                return candidate
    return res

cyclic_string = 'a'
# check that your code works correctly on provided example
assert shortestCycle(cyclic_string) == 1, 'Wrong answer'

cyclic_string = 'aa'
# check that your code works correctly on provided example
assert shortestCycle(cyclic_string) == 1, 'Wrong answer'

cyclic_string = 'aca'
# check that your code works correctly on provided example
assert shortestCycle(cyclic_string) == 3, 'Wrong answer'

cyclic_string = 'acac'
# check that your code works correctly on provided example
assert shortestCycle(cyclic_string) == 2, 'Wrong answer'