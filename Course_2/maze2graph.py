# Question 3
# Given a maze, where empty cells are represented by a '.',
# walls are represented by '#' and the exit is represented by 'X',
# construct an adjacency list where the vertices are empty cells and
# the exit and the edges represent that one non-wall cell shares a side with the other one.

def maze2graph(maze):
    height, width = len(maze), len(maze[0])
    graph = {(x, y): [] for y in range(width) for x in range(height) if maze[x][y] != "#"}
    for vertex in graph:
        i, j = vertex
        for candidate in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if candidate in graph:
                graph[vertex].append(candidate)
    # YOUR CODE GOES HERE

    return graph

if __name__ == "__main__":
    maze = ['....#.']
    # check that your code works correctly on provided example
    print(maze2graph(maze))
    assert maze2graph(maze) == {(0, 0): [(0, 1)], (0, 1): [(0, 0), (0, 2)],
                                (0, 2): [(0, 1), (0, 3)], (0, 3): [(0, 2)],
                                (0, 5): []}, 'Wrong answer'