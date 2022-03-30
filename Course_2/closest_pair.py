# Given an adjacency matrix of a directed graph with weights of edges instead
# of 0 and 1 (if there is no edge between the vertices that value is replaced
# with float("inf")), find the pair of vertices with the minimum shortest path
# among all pairs of vertices. If there are several such pairs, output any of them.
#
# If there is no such pair, output (-1, -1).

from copy import deepcopy

def closestPair(weight_matrix):
    n = len(weight_matrix)
    closest_pair = (-1, -1)
    dist = deepcopy(weight_matrix)
    min_dist = float("inf")
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if dist[i][j] < min_dist:
                min_dist = dist[i][j]
                closest_pair = (i, j)
    print(dist)
    return closest_pair

if __name__ == "__main__":
    weight_matrix = [[float('inf'), 5, 2],
                     [5, float('inf'), 1],
                     [2, 1, float('inf')]]
    # check that your code works correctly on provided example
    print(closestPair(weight_matrix))
    assert closestPair(weight_matrix) == (1, 2), 'Wrong answer'