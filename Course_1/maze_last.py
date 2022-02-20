import math
import random


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
            result = min(result, weighted_escape_length(maze, w, a, b, jumps))
        elif 0 <= a < n and 0 <= b < m and maze[a][b] == 1:
            result = min(result, weighted_escape_length(maze, w, a, b, jumps+w-1, 1))
    maze[i][j] = maze_w
    return result


def fastest_escapes_recursion(maze, w, i, j, current_depth, shortest_path, maze_w=0):
    n = len(maze)
    m = len(maze[0])
    current_depth += 1
    if i == n - 1 and j == m - 1 and current_depth == shortest_path:
        return [[(i, j)]]
    maze[i][j] = 2
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            hop = fastest_escapes_recursion(maze, w, a, b, current_depth, shortest_path)
            for s in hop:
                result.append([(i, j)] + s)

        if 0 <= a < n and 0 <= b < m and maze[a][b] == 1:
            hop = fastest_escapes_recursion(maze, w, a, b, current_depth+w-1, shortest_path, 1)
            for s in hop:
                result.append([(i, j)] + s)
    maze[i][j] = maze_w
    return result


def weighted_escapes(maze, w):
    shortest_path = weighted_escape_length(maze, w)
    result = fastest_escapes_recursion(maze, w, 0, 0, 0, shortest_path)
    return result


if __name__ == "__main__":
    test_aa = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0]
    ]
    #print(weighted_escapes(test_aa, 0))

    test_a = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    test_b = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]

    test_c = [
      [0, 0, 0],
      [1, 0, 0],
      [1, 1, 0]
    ]
    # should print [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]]
    #print(weighted_escapes(test_b, 0))
    # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    # the order of the paths within the list might be different
    #print(weighted_escapes(test_b, 2))

    #print(weighted_escapes(test_c, 5))
    for i in range(0):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        w = random.randint(1, 5)
        maze = [[random.randint(0, 1) for _ in range(b)] for _ in range(a)]
        maze[0][0] = 0
        maze[-1][-1] = 0
        #print(weighted_escapes(maze, w))
