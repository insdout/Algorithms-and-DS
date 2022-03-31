# Given an adjacency matrix with weights of edges instead of 0 and 1
# (if there is no edge between the vertices that value is replaced with float("inf"))
# and a pair of vertices find the shortest path between those vertices and output this path,
# starting with vertex v_from and ending with vertex v_to.
#
# If there is no such path output -1.

from heapq import heappop, heappush


def dijkstraPath(adj_matrix, v_from, v_to):
    graph, n = adj_matrix, len(adj_matrix)
    # HINT: use a parent array to store a parent for each vertice
    heap, path = [], []
    used = [False for i in range(n)]
    distance = [float("inf") for i in range(n)]
    parent_list = [False for i in range(n)]
    heappush(heap, (0, v_from))
    distance[v_from] = 0

    while len(heap) > 0:
        d, v = heappop(heap)
        used[v] = True

        if distance[v] < d:
            continue

        for u, c in enumerate(adj_matrix[v]):
            if not used[u] and c != float("inf") and d + c < distance[u]:
                distance[u] = d + c
                heappush(heap, (distance[u], u))
                parent_list[u] = v
    #print(distance)
    #print(parent_list)
    if distance[v_to] == float("inf") \
            or (v_from == v_to and adj_matrix[v_from][v_to] == float("inf")):
        return -1
    #path.append(v_from)
    if v_from == v_to and adj_matrix[v_from][v_to] != float("inf"):
        return [v_from]

    if parent_list[v_to] is not False or v_from == v_to:
        while v_to is not False:
            #print("v_from", v_to)
            path.insert(0, v_to)
            v_to = parent_list[v_to]


    return path

if __name__ == "__main__":
    adj_matrix = [[0, 5, 2],
                  [5, float('inf'), float('inf')],
                  [2, float('inf'), float('inf')]]
    v_from, v_to = 0, 0
    # check that your code works correctly on provided example
    print(dijkstraPath(adj_matrix, v_from, v_to))

    adj_matrix = [[float('inf'), 5, 2],
                  [5, float('inf'), float('inf')],
                  [2, float('inf'), float('inf')]]
    v_from, v_to = 0, 0
    # check that your code works correctly on provided example
    print(dijkstraPath(adj_matrix, v_from, v_to))

    #assert dijkstraPath(adj_matrix, v_from, v_to) == [0, 2], 'Wrong answer'
    adj_matrix = [[float('inf'), 5, 2],
                  [5, float('inf'), float('inf')],
                  [2, float('inf'), float('inf')]]
    v_from, v_to = 0, 2
    # check that your code works correctly on provided example
    print(dijkstraPath(adj_matrix, v_from, v_to))
    assert dijkstraPath(adj_matrix, v_from, v_to) == [0, 2], 'Wrong answer'