#

def countingsort(array, lowerbound, upperbound):
    n = len(array)
    sorted_array = []
    count = [0 for i in range(lowerbound, upperbound + 1)]

    for element in array:
        count[element - lowerbound] += 1
    print(count)
    for index, element in enumerate(count):
        sorted_array.extend([lowerbound + index for _ in range(count[index])])
        print("sorted:", sorted_array)
    return sorted_array

arr = [3, 2, 1]
lowerbound = 1
upperbound = 3
# check that your code works correctly on provided example
assert countingsort(arr, lowerbound, upperbound) == [1, 2, 3], 'Wrong answer'

arr = []
lowerbound = 0
upperbound = 10
# check that your code works correctly on provided example
assert countingsort(arr, lowerbound, upperbound) == [], 'Wrong answer'

arr = [5, 2]
lowerbound = 2
upperbound = 5
# check that your code works correctly on provided example
assert countingsort(arr, lowerbound, upperbound) == [2,5], 'Wrong answer'