# Question 2
# Given an adjacency list for a graph determine if a graph is bipartite.
# (A graph is bipartite if it's vertices can be divided in to two sets such
# that there is no edges between vertices that are in the different sets).

from collections import deque


def isBipartite(adj_list):
    n = len(adj_list)
    is_bipartite = True

    Q = deque()
    visited = [False for i in range(n)]
    color = [0 for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            Q.append(v)
            color[v] = 1
            while len(Q) > 0:
                cur_v = Q.popleft()
                cur_color = color[cur_v]
                for neighbor in adj_list[cur_v]:
                    if not visited[neighbor]:
                        Q.append(neighbor)
                        color[neighbor] = (cur_color + 1) % 2
                        visited[neighbor] = True
                    elif color[neighbor] == cur_color:
                        is_bipartite = False
    return is_bipartite

if __name__ == "__main__":
    print("1st case.")
    adj_list = [[], [2], [1]]
    # check that your code works correctly on provided example
    print(isBipartite(adj_list))
    assert isBipartite(adj_list), 'Wrong answer'

    print("2nd case.")
    adj_list = [[1], [2], [0]]
    # False
    print(isBipartite(adj_list))
    assert not isBipartite(adj_list), 'Wrong answer'

    print("3nd case.")
    adj_list = [[1], []]
    # True
    print(isBipartite(adj_list))
    assert isBipartite(adj_list), 'Wrong answer'

    print("4nd case.")
    adj_list = [[], []]
    # True
    print(isBipartite(adj_list))
    assert isBipartite(adj_list), 'Wrong answer'

    print("5nd case.")
    adj_list = [[1], [2], [3], [0]]
    # True
    print(isBipartite(adj_list))
    assert isBipartite(adj_list), 'Wrong answer'

    print("6nd case.")
    adj_list = [[1], [2], [3, 0], [0]]
    # False
    print(isBipartite(adj_list))
    assert not isBipartite(adj_list), 'Wrong answer'

    print("7nd case.")
    adj_list = [[1], [2], [3, 0], [0], []]
    # False
    print(isBipartite(adj_list))
    assert not isBipartite(adj_list), 'Wrong answer'

    print("8nd case.")
    adj_list = [[1], [2, 4], [3], [0, 4], []]
    # True
    print(isBipartite(adj_list))
    assert isBipartite(adj_list), 'Wrong answer'

    print("9nd case.")
    adj_list = [[1], [2], [3, 4], [0], []]
    # True
    print(isBipartite(adj_list))
    assert isBipartite(adj_list), 'Wrong answer'

    print("9nd case.")
    adj_list = [[1], [2], [3, 4], [0, 4], []]
    # False
    print(isBipartite(adj_list))
    assert not isBipartite(adj_list), 'Wrong answer'

    print("9nd case.")
    adj_list = [[1, 3], [0, 2], [1, 3], [0, 4], [3]]
    # True
    print(isBipartite(adj_list))
    assert isBipartite(adj_list), 'Wrong answer'

    print("9nd case.")
    adj_list = [[1, 3], [0, 2], [1, 3], [0, 4], [3, 2]]
    # False
    print(isBipartite(adj_list))
    assert not isBipartite(adj_list), 'Wrong answer'