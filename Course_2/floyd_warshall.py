# Question 1
# Given an adjacency matrix with weights of edges instead of 0 and 1
# (if there is no edge between the vertices that value is replaced with float("inf")),
# compute the matrix of shortest paths between all pairs of vertices
# using the Floyd-Warshall algorithm.

from copy import deepcopy


def FloydWarshall(weight_matrix):
    n = len(weight_matrix)
    dist = deepcopy(weight_matrix)
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # YOUR CODE GOES HERE

    return dist

if __name__ == "__main__":
    weight_matrix = [[float('inf'), 5, 2],
                     [5, float('inf'), 1],
                     [2, 1, float('inf')]]
    # check that your code works correctly on provided example
    print(FloydWarshall(weight_matrix))
    assert FloydWarshall(weight_matrix) == [[0, 3, 2], [3, 0, 1], [2, 1, 0]], 'Wrong answer'