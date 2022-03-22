# Question 3
# Given a maze, where empty cells are represented by a '.',
# walls are represented by '#' and the exit is represented by 'X',
# construct an adjacency list where the vertices are empty cells and
# the exit and the edges represent that one non-wall cell shares a side with the other one.

def maze2graph(maze):
    height, width = len(maze), len(maze[0])
    graph = {(x, y): [] for y in range(width) for x in range(height) if maze[x][y] != "#"}

    # YOUR CODE GOES HERE

    return graph

if __name__ == "__main__":
    maze = ['....#.']
    # check that your code works correctly on provided example
    assert maze2graph(maze) == {(0, 0): [(0, 1)], (0, 1): [(0, 0), (0, 2)],
                                (0, 2): [(0, 1), (0, 3)], (0, 3): [(0, 2)],
                                (0, 5): []}, 'Wrong answer'