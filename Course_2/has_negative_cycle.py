# Given an adjacency matrix with weights of edges instead of 0 and 1
# (if there is no edge between the vertices that value is replaced with float("inf")),
# return True if there is a cycle with negative cost in the graph and False if there is no such cycle.


def hasNegativeCycle(weight_matrix):
    n = len(weight_matrix)
    has_negative_cycle = False
    dist = [float("inf") for _ in range(n)]
    for start in range(n):
        if dist[start] == float("inf"):
            dist[start] = 0
            print("start:", start)
            for _ in range(n):
                for i in range(n):
                    for j in range(n):
                        if weight_matrix[i][j] == float("inf"):
                            continue
                        if dist[j] > dist[i] + weight_matrix[i][j]:
                            dist[j] = dist[i] + weight_matrix[i][j]

            for i in range(n):
                for j in range(n):
                    if weight_matrix[i][j] == float("inf"):
                        continue
                    if dist[j] > dist[i] + weight_matrix[i][j]:
                        has_negative_cycle = True
                        return has_negative_cycle
    # YOUR CODE GOES HERE

    return has_negative_cycle

if __name__ == "__main__":
    weight_matrix = [[float('inf'), 5, 2],
                     [5, float('inf'), -10],
                     [2, -10, float('inf')]]
    # check that your code works correctly on provided example
    assert hasNegativeCycle(weight_matrix), 'Wrong answer'

    weight_matrix = [[float('inf'), 1, float('inf'), 2, float('inf'), float('inf')],
                     [float('inf'), float('inf'), -3, 2, float('inf'), float('inf')],
                     [float('inf'), float('inf'), float('inf'), 3, float('inf'), 1],
                     [float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf')],
                     [float('inf'), float('inf'), 1, 1, float('inf'), 1],
                     [float('inf'), float('inf'), 1, float('inf'), float('inf'), float('inf')]]
    assert not hasNegativeCycle(weight_matrix), 'Wrong answer'

    weight_matrix = [[float('inf'), 1, float('inf'), 2, float('inf'), float('inf')],
                     [float('inf'), float('inf'), -3, 2, float('inf'), float('inf')],
                     [float('inf'), 1, float('inf'), float('inf'), float('inf'), 1],
                     [float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf')],
                     [float('inf'), float('inf'), 1, 1, float('inf'), 1],
                     [float('inf'), float('inf'), 1, float('inf'), float('inf'), float('inf')]]
    assert hasNegativeCycle(weight_matrix), 'Wrong answer'