# Given the size of the chess board NxN and the coordinates of rooks,
# placed on the board, determine the minimum possible number of rooks
# left after performing the following operation:
#
# Select two rooks so that attack each other (they are on the same row
# or column of the board) and have one of them captures the other
# (remove one of them from the board)
#
# Repeat until there are no two rooks attacking each other.

def iterativeDFS(adjList, v, discovered):
    path = []
    stack = []
    stack.append(v)

    while len(stack) > 0:
        v = stack.pop()
        if discovered[v]:
            continue
        discovered[v] = True
        #print(v, end=' ')
        path.append(v)
        neighbours = adjList[v]
        for u in neighbours:
            if not discovered[u]:
                stack.append(u)
    return path


def minRooksLeft(board_size, coordinates):
    # each entry in coordinates array looks like this: (x, y) - coordinates of the rook
    n = len(coordinates)
    rooks_left = 0
    adjacency_list = [[] for _ in range(n)]
    print(adjacency_list, n)
    for ind, coordinate in enumerate(coordinates):
        for i in range(ind):
            if coordinate[0] == coordinates[i][0] or coordinate[1] == coordinates[i][1]:
                adjacency_list[ind].append(i)
                adjacency_list[i].append(ind)
                print(adjacency_list)
    visited = [False for _ in range(n)]
    for edge in range(n):
        if not visited[edge]:
            rooks_left += 1
            cur_path = iterativeDFS(adjacency_list, edge, visited)
            for visited_edge in cur_path:
                visited[visited_edge] = True

    # YOUR CODE GOES HERE

    return rooks_left


if __name__ == "__main__":

    print("Case 1")
    board_size = 4
    coordinates = [(0, 0), (0, 3), (3, 0)]
    # check that your code works correctly on provided example
    assert minRooksLeft(board_size, coordinates) == 1, 'Wrong answer'
    print(minRooksLeft(board_size, coordinates))

    print("Case 2")
    board_size = 4
    coordinates = [(0, 0), (1, 1), (2, 2)]
    print(minRooksLeft(board_size, coordinates))
    