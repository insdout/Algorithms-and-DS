import math
def foobar(a):
    return a


def weighted_escapes(maze, w, i=0, j=0,  maze_w=0):
    foo = foobar(1)
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


test_a = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    # should print 5
print("==============================")
print(weighted_escapes(test_a,1))

test_b = [
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
# should print 5
print("==============================")
# print(fastest_escape_length(test_a))
print(weighted_escapes(test_b,1))