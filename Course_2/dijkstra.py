# Given an adjacency matrix with weights of edges instead of 0 and 1
# (if there is no edge between the vertices that value is replaced with float("inf"))
# and a pair of vertices v_form and v_to find the shortest path between
# those vertices using the Dijkstra's algorithm.
#
# If there is no such path output -1.

from heapq import heappop, heappush


def dijkstra(adj_matrix, v_from, v_to):
    n, graph = len(adj_matrix), adj_matrix

    distance = [float("inf") for i in range(n)]
    heap = []
    used = [False for i in range(n)]
    prev = [False for i in range(n)]
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
                prev[u] = v

    # YOUR CODE GOES HERE

    return distance[v_to], prev

if __name__ == "__main__":
    adj_matrix = [[float('inf'), 5, 2],
                  [5, float('inf'), float('inf')],
                  [2, float('inf'), float('inf')]]
    v_from, v_to = 0, 2
    print(dijkstra(adj_matrix, v_from, v_to))
    # check that your code works correctly on provided example
    #assert dijkstra(adj_matrix, v_from, v_to) == 2, 'Wrong answer'