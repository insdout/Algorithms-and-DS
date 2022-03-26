# Given an adjacency matrix for an undirected graph and a vertex,
# modify the dfs algorithm to output the number of vertices in the
# same graph component as the given one (counting the given one).
#
# The function must work correctly when called several times, e.g.
# don't use global variables or test it by calling more than once.

graph = []
visited = []


def dfs(v):
    global visited
    res = 1
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            res += dfs(u)
    return res



def sameComponent(adj_list, vertex):
    global graph, visited
    n = len(adj_list)
    adj_list_l = [[i for i, val in enumerate(adj_list[j]) if val == 1] for j in range(n)]
    graph = adj_list_l
    n = len(graph)
    visited = [False for i in range(n)]
    vertex_count = 0

    vertex_count += dfs(vertex)

    return vertex_count


if __name__ == "__main__":
    adj_matrix = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    vertex = 0
    # check that your code works correctly on provided example
    print(sameComponent(adj_matrix, vertex))
    assert sameComponent(adj_matrix, vertex) == 3, 'Wrong answer'

    adj_matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    vertex = 0
    # check that your code works correctly on provided example
    print(sameComponent(adj_matrix, vertex))
    assert sameComponent(adj_matrix, vertex) == 3, 'Wrong answer'

    adj_matrix = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    vertex = 0
    # check that your code works correctly on provided example
    print(sameComponent(adj_matrix, vertex))
    assert sameComponent(adj_matrix, vertex) == 2, 'Wrong answer'

    adj_matrix = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    vertex = 2
    # check that your code works correctly on provided example
    print(sameComponent(adj_matrix, vertex))
    assert sameComponent(adj_matrix, vertex) == 1, 'Wrong answer'

    adj_matrix = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    vertex = 2
    # check that your code works correctly on provided example
    print(sameComponent(adj_matrix, vertex))
    assert sameComponent(adj_matrix, vertex) == 1, 'Wrong answer'

    vertex = 0
    # check that your code works correctly on provided example
    print(sameComponent(adj_matrix, vertex))
    assert sameComponent(adj_matrix, vertex) == 2, 'Wrong answer'


