from bisect import bisect_left


def maxArea(height: list[int]) -> int:
    stack_ind = []
    stack_h = []
    water = 0
    for ind in range(len(height)):
        if len(stack_ind) == 0:
            stack_ind.append(ind)
            stack_h.append(height[ind])
        if height[ind] > height[stack_ind[-1]]:
            stack_ind.append(ind)
            stack_h.append(height[ind])
        else:
            first_h = bisect_left(stack_h, height[ind])
            water = max(water, (ind - stack_ind[first_h]) * min(height[ind], stack_h[first_h]))
    stack_ind = []
    stack_h = []
    for ind in reversed(range(len(height))):
        if len(stack_ind) == 0:
            stack_ind.append(ind)
            stack_h.append(height[ind])
        if height[ind] > height[stack_ind[-1]]:
            stack_ind.append(ind)
            stack_h.append(height[ind])
        else:
            first_h = bisect_left(stack_h, height[ind])
            water = max(water, (stack_ind[first_h] - ind) * min(height[ind], stack_h[first_h]))
    return water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))

height = [1, 2, 4, 3]
print(maxArea(height))
