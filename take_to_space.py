def take_to_space(mass, C):
    if len(mass) == 0:
        if C >= 0:
            return {tuple()}
        else:
            return set()
    without_last = take_to_space(mass[:-1], C)
    last = len(mass)-1
    with_last = take_to_space(mass[:-1], C - mass[-1])
    result = without_last
    for s in with_last:
        result.add(s + tuple([last]))
    return result

if __name__ == "__main__":
# should print {(), (0,), (1,), (2,), (0, 1)}
# elements of the set can be printed in a different order
    print(take_to_space([1, 2, 3], 3))