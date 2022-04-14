# You are given a list of names, each name is not longer than 20 characters.
# Return them sorted in an increasing order, using the Radix Sort algorithm.

def counting_sort(arr, power, lowerbound, upperbound, max_power):
    n = len(arr)
    base = upperbound - lowerbound + 1
    count = [[] for _ in range(base)]
    sorted_array = []
    for name in arr:
        rel_index = max_power - len(name)
        ev_index = ord(name[-(power - rel_index + 1)]) - lowerbound \
            if power >= rel_index else base - 1
        count[ev_index].append(name)
    for i in range(base):
        sorted_array.extend(count[i])
    return sorted_array

def radixsort(names):
    n = len(names)
    if n <= 1:
        return names
    lowerbound = ord("A")
    upperbound = ord("z")
    max_power = max([len(element) for element in names])
    for power in range(max_power):
        names = counting_sort(names, power, lowerbound, upperbound, max_power)
        print(names)
    return names



arr = []
# check that your code works correctly on provided example
assert radixsort(arr) == [], 'Wrong answer'

arr = ['Ivan', 'John', 'Anna']
# check that your code works correctly on provided example
assert radixsort(arr) == ['Anna', 'Ivan', 'John'], 'Wrong answer'

arr = ["abc","ba", "bb"]
# check that your code works correctly on provided example
assert radixsort(arr) == sorted(arr), 'Wrong answer'


arr = ['Zaxb', 'Az', 'Bxa', "Ab", "Ba", 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
# check that your code works correctly on provided example
print("started")
assert radixsort(arr) == sorted(arr), 'Wrong answer'
arr = ['Zaxb', 'Az', 'Bxa', "Ab", "Ba", 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
# check that your code works correctly on provided example


arr = ['rnwpokagbedccklebldl', 'ipntxcdfbklidlpyinhc', 'yzywdzjhjjotkohzlgjr', 'sactfpjddqzwfvrizzbn', 'rbehwjmmgcbxchnjtqhp', 'qgubrnndaftujxmxokbv', 'uqljfiufozbmrnudaunh', 'bvwphkeqwddnbxstvefa', 'xwwpaghacncxlztoduxx', 'ikeqvczroozolsyhjqbf']
sorted_arr = ['bvwphkeqwddnbxstvefa', 'ikeqvczroozolsyhjqbf', 'ipntxcdfbklidlpyinhc', 'qgubrnndaftujxmxokbv', 'rbehwjmmgcbxchnjtqhp', 'rnwpokagbedccklebldl', 'sactfpjddqzwfvrizzbn', 'uqljfiufozbmrnudaunh', 'xwwpaghacncxlztoduxx', 'yzywdzjhjjotkohzlgjr']
assert radixsort(arr) == sorted_arr, 'Wrong answer'


arr = ["asasw", "Asanxs", "ashdcx", "Ghs", "A"]
# check that your code works correctly on provided example
print("started")
assert radixsort(arr) == sorted(arr), 'Wrong answer'