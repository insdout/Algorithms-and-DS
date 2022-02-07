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