# Given an adjacency matrix with weights of edges instead of 0 and 1
# (if there is no edge between the vertices that value is replaced with float("inf")),
# and a source vertex v_from, return a distance array of the shortest path distances
# from this vertex to all others.


def BellmanFord(weight_matrix, v_from):
    n, graph = len(weight_matrix), weight_matrix
    dist = [float("inf") for i in range(n)]

    dist[v_from] = 0
    for _ in range(n-1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == float("inf"):
                    continue
                if dist[j] > dist[i] + graph[i][j]:
                    dist[j] = dist[i] + graph[i][j]

    # YOUR CODE GOES HERE

    return dist

if __name__ == "__main__":
    weight_matrix = [[float('inf'), 5, 2],
                     [5, float('inf'), float('inf')],
                     [2, float('inf'), float('inf')]]
    v_from = 0
    # check that your code works correctly on provided example
    print(BellmanFord(weight_matrix, v_from))
    assert BellmanFord(weight_matrix, v_from) == [0, 5, 2], 'Wrong answer'

    weight_matrix = [[float('inf'), 1, float('inf'), 2, float('inf'), float('inf')],
                     [float('inf'), float('inf'), -3, 2, float('inf'), float('inf')],
                     [float('inf'), float('inf'), float('inf'), 3, float('inf'), 1],
                     [float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf')],
                     [float('inf'), float('inf'), 1, 1, float('inf'), 1],
                     [float('inf'), float('inf'), 1, float('inf'), float('inf'), float('inf')]]
    v_from = 0
    # check that your code works correctly on provided example
    print(BellmanFord(weight_matrix, v_from))
    #assert BellmanFord(weight_matrix, v_from) == [0, 5, 2], 'Wrong answer'
