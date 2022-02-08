# In one of the lectures this week, we have designed a recursive algorithm using so-called backtracking
# to find whether a packman will escape from a maze. More formally,
#
# Input: a maze defined by a 2-d array maze where
# maze[i][j] is equal to 0 if the j-th cell on the i-th row is empty
# and 1 if there is a wall there. It is guaranteed that the upper left and lower right cells are empty.
#
# Output: True if there exists a path from the upper left cell to the lower right cell passing
# through empty cells only. False otherwise. A path can go from a cell to a cell that shares a side with it.
#
# Below is a python implementation of the algorithm we have designed.

# In this assignment, you will be asked to develop this code in different directions.
#
# Part 1. Write a function fastest_escape_length(maze) that takes a maze (as above)
# as input and returns the length of the shortest path from the upper left corner
# to the lower right corner. The length of a path is the number of cells it passes through.
# If there is no path, the function should return math.inf.
#
# For example, if
# maze = [
#       [0, 0, 0],
#       [1, 0, 0],
#       [1, 1, 0]
#     ]
# Hint: In the function can_escape above, you can return the length of the shortest
# path instead of True and  math.inf instead of False. Therefore, you can build your
# solution upon the provided code.
#
# Part 2. Write a function fastest_escapes(maze) that takes a maze and returns
# a list of all shortest paths from the upper left corner to the lower right corner.
# Each path should be represented as a list of cells along the path where a cell is
# a tuple of the coordinates. In the example above, the output should be
# [ [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
#
# Hint:  A good starting point would be the previous part. You now should modify it
# ot to just return the length of the shortest path but a list of all the shortest
# paths instead. At each recursive call, we take all the fastest escapes for the
# neighbors, take only the ones of the shortest length, and extend them by one.
#
# Part 3. Write a function weighted_escape_length(maze, w) that takes a maze and a
# nonegative integer w and returns the length of the shortest path from the upper
# left corner to the lower right corner if it is allowed to pass through the walls,
# but each wall is considered equivalent to w empty cells.
#
# For example, for the example above and w = 0 (that is, passing through walls is for free),
# the result should be 2.
#
# Hint. A solution can be obtained as a modification of your solution of the part 1
# but now taking into account the option of passing through the wall and the corresponding penalty.
#
# Part 4. Write a function weighted_escapes(maze, w) that returns a list of shortest
# paths in the sense of Part 3. For example, for the sample input of Part 3, the output
# should be [ [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)] ].
#
# The time limit for each test will be one second.


import math
def can_escape(maze, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return True
    maze[i][j] = 1
    result = False
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            result = result or can_escape(maze, a, b)
    maze[i][j] = 0
    return result

def fastest_escape_length(maze, i=0, j=0, jumps=0):
    n = len(maze)
    m = len(maze[0])
    jumps += 1
    if i == n - 1 and j == m - 1:
        return jumps
    maze[i][j] = 1
    result = math.inf
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            result = min(result, fastest_escape_length(maze, a, b, jumps))
    maze[i][j] = 0
    return result

def fastest_escapes(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[(i, j)]]
    maze[i][j] = 1
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            hop = fastest_escapes(maze, a, b)
            for s in hop:
                result.append([(i, j)] + s)
                    # print(result)

    l = []
    if result:
        min_len = min([len(s) for s in result])
    else:
        min_len = 0
    for el in result:
        if el not in l and len(el) == min_len:
            l.append(el)
    result = l

    maze[i][j] = 0
    return result

def weighted_escape_length(maze, w, i=0, j=0, jumps=0, maze_w=0):
    n = len(maze)
    m = len(maze[0])
    jumps += 1
    if i == n - 1 and j == m - 1:
        return jumps
    maze[i][j] = 2
    result = math.inf
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            result = min(result, weighted_escape_length(maze,w, a, b, jumps))
        elif 0 <= a < n and 0 <= b < m and maze[a][b] == 1:
            result = min(result, weighted_escape_length(maze, w,a, b, jumps+w-1,1))
    maze[i][j] = maze_w
    return result

def weighted_escapes(maze, w, i=0, j=0,  maze_w=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[(i, j)]]
    maze[i][j] = 2
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            hop = weighted_escapes(maze,w, a, b)
            for s in hop:
                result.append([(i, j)] + s)
                # print(result)
        elif 0 <= a < n and 0 <= b < m and maze[a][b] == 1:
            hop = weighted_escapes(maze, w, a, b,1)
            for s in hop:
                result.append([(i, j)] + s)

    maze[i][j] = maze_w
    min_l =[]
    new_res = []
    for l in result:
        path_len = 0
        for a,b in l:
            path_len += maze[a][b] * w + 1 - maze[a][b]
        min_l.append(path_len)
    if min_l:
        minimal_length = min(min_l)
    else:
        minimal_length =0
    for l in result:
        path_len = 0
        for a, b in l:
            path_len += maze[a][b] * w + 1 - maze[a][b]
        if path_len == minimal_length and l not in new_res:
            new_res.append(l)

    result = new_res
        #print(l, len(l), min_l, sep="\n")
    return result


# some test code
if __name__ == "__main__":
    test_aa = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(fastest_escapes(test_aa))


    test_a = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    # should print 5
    print(fastest_escape_length(test_a))
    # should print 2
    print(weighted_escape_length(test_a, 0))
    test_b = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    # should print inf
    print(fastest_escape_length(test_b))
    # should print 5
    print(weighted_escape_length(test_b, 1))
    # should print 6
    print(weighted_escape_length(test_b, 2))

    # should print [[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    print(fastest_escapes(test_a))
    # should print []
    print("===========")
    print(test_b)
    print("===========")
    print(fastest_escapes(test_b))
    # should print [5, 5, 5, 5, 5, 5]
    print(list(map(len, fastest_escapes([[0 for _ in range(3)] for _ in range(3)]))))
    print("===========")
    print(test_b)
    print("===========")
    # should print [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]]
    print(weighted_escapes(test_b, 0))
    # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    # the order of the paths within the list might be different
    print(weighted_escapes(test_b, 2))
