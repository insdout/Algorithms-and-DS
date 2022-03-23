# Given a maze, where empty cells are represented by a '.',
# walls are represented by '#' and the exit is represented by 'X',
# and the coordinates of the agent in the maze, output the shortest
# path to the exit as a string containing 4 different letters:
# "U", "D", "L", "R" for going up, down, left and right respectively.
# If there is no such path, output -1.

from collections import deque


def path2exit(maze, x, y):
    height, width = len(maze), len(maze[0][0])
    path = []
    v_to = False
    graph = {(x, y): [] for y in range(width) for x in range(height) if maze[x][0][y] != "#"}
    for vertex in graph:
        i, j = vertex
        if maze[i][0][j] == "X":
            v_to = (i, j)
        for candidate in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if candidate in graph:
                graph[vertex].append(candidate)
    print(graph)
    visited = {v: False for v in graph.keys()}
    Q = deque()
    v_from = (x, y)
    Q.append((path, v_from))
    visited[v_from] = True
    while len(Q) > 0 and v_from is not False:
        cur_path, cur_v = Q.pop()
        print("cur v",cur_v, Q)
        if cur_v == v_to:
            path = cur_path
            break
        for neighbor in graph[cur_v]:
            if not visited[neighbor]:
                temp_path = [v for v in cur_path]
                y_dir = neighbor[0] - cur_v[0]
                x_dir = neighbor[1] - cur_v[1]
                print(cur_v, neighbor, x_dir, y_dir, cur_path)
                if x_dir == -1 and y_dir == 0:
                    temp_path.append("L")
                elif x_dir == 1 and y_dir == 0:
                    temp_path.append("R")
                elif x_dir == 0 and y_dir == 1:
                    temp_path.append("D")
                elif x_dir == 0 and y_dir == -1:
                    temp_path.append("U")
                else:
                    raise ValueError('Not neighbor found!')
                Q.append((temp_path, neighbor))
                visited[neighbor] = True
    # YOUR CODE GOES HERE

    if len(path) == 0:
        return -1
    return ''.join(path)


if __name__ == "__main__":
    maze = [['.#.'], ['..X']]
    x, y = 0, 0
    # check that your code works correctly on provided example
    print(path2exit(maze, x, y))
    assert path2exit(maze, x, y) == 'DRR', 'Wrong answer'

    print()
    maze = [['.#.'], ['...'], ['..X']]
    x, y = 0, 0
    # check that your code works correctly on provided example
    print(path2exit(maze, x, y))
    #assert path2exit(maze, x, y) == 'DRR', 'Wrong answer'