# A landscape in a Flat World consists of blocks size 1 by 1 meter.
# The island is a set of different height columns consist of stone and surrounded by the sea.
# Heavy rain have fallen over the island, and filled all the lowlands with water. Extra water
# has gone back into the sea, without increasing its level. According to the landscape of the
# island, determine how many blocks of water remain after rain in the lowlands on the island.
#
# Implement a function calc_rain_water(h) which takes the landscape of the island and returns
# the number of remaining water blocks.
#
# Input data:
# List hh consisting of integers, each number corresponds to island column height,
# len(h) ≤100000,  h_i  1 ≤ h ≤10^9.
#
# Output data:
# One integer — remaining water blocks number.
# Example:
#
# Input: h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]Input:h=[2,5,2,3,6,9,1,3,4,6,1]
#
# Output: 15
# To satisfy time limit for this task your solution has to work for O(n)O(n).
# Try to use the same approach with stack like in Maximum rectangle in a histogram task.


def calc_rain_water(h):
    stack_ind = []
    water = 0
    #print("h:", *h)
    if len(h) < 2:
        return None
    for i in range(0, len(h)):
        #print("h:", h[i], "stack:", *map(lambda x: h[x], stack_ind))
        while stack_ind and h[i] > h[stack_ind[-1]]:
            last_pos = stack_ind.pop()
            last_height = h[last_pos]
            #print("pop_p", last_pos, "pop_h", last_height)
            if len(stack_ind) == 0:
                break
            #print(min(h[i], h[stack_ind[-1]]), (i - stack_ind[-1] - 1))
            water += (min(h[i], h[stack_ind[-1]]) - last_height) *\
                     (i - stack_ind[-1] - 1)
            #print("water", water)
        stack_ind.append(i)
    return water

# some test code
if __name__ == "__main__":
    test_h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]
    # should print 15
    print(calc_rain_water(test_h))

    test_h = [2, 4, 6, 8, 6, 4, 2]
    # should print 0
    print(calc_rain_water(test_h))

    test_h = [8, 6, 4, 2, 4, 6, 8]
    # should print 18
    print(calc_rain_water(test_h))