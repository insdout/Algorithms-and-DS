# from here:
# https://en.wikipedia.org/wiki/Binary_search_algorithm

#TODO: разобраться

def binary_search_rightmost(l, target):
    left = 0
    right = len(l)
    while left < right:
        mid = (left + right) // 2
        print("left:", left, "mid:", mid, "right", right)
        if l[mid] > target:
            right = mid
        else:
            left = mid + 1
        print("left:", left, "mid:", mid, "right", right)
        print()
    return right - 1

if __name__ == "__main__":
    a = [1, 2]
    print(binary_search_rightmost(a, 2))