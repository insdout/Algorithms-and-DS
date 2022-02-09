# There are nn very helpful devices that could be taken to the space station.
# You are given a list mass of their masses and the total capacity C of your rocket.
# You would like to generate all lists of devices that could be taken to the station
# with a single launch of a rocket. Write a functions take_to_space(mass, C) that would
# return a set of all feasible tuples of devices. Devices should be given by their indices
# (not masses!) in increasing order.
#
# For example, if mass = [1, 2, 3] and C = 3, the output should be {(), (0,), (1,), (2,), (0, 1)}.
#
# Hint: look at the function for the Subset Sum problem.


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
