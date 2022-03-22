# Given an undirected (and unweighted) graph and a pair
# of vertices find the shortest path between a pair of vertices.
# Return -1 if vertices is not connected.

from collections import deque


def distance(adj_list, v_from, v_to):
    n = len(adj_list)
    distance = -1

    visited = [False for i in range(n)]
    Q = deque()
    Q.append((distance + 1, v_from))
    visited[v_from] = True
    while len(Q) > 0:
        cur_dist, cur_v = Q.pop()
        if cur_v == v_to:
            distance = cur_dist
        for neighbor in adj_list[cur_v]:
            if not visited[neighbor]:
                Q.append((cur_dist + 1, neighbor))
                visited[neighbor] = True
    # YOUR CODE GOES HERE

    return distance

if __name__ == "__main__":

    adj_list = [[1], [0, 2], [1]]
    v_from, v_to = 0, 2
    # check that your code works correctly on provided example
    print(distance(adj_list, v_from, v_to))
    assert distance(adj_list, v_from, v_to) == 2, 'Wrong answer'

