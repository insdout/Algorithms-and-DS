def reverseGraph(adj_list):
    # Given an adjacency list of a directed graph,
    # reverse it (change the direction of all edges)
    # and output it as an adjacency list
    n = len(adj_list)
    reversed_graph = [[] for i in range(n)]
    for index, edges in enumerate(adj_list):
        for edge in edges:
            # noinspection PyTypeChecker
            reversed_graph[edge].append(index)
    return reversed_graph


adj_list = [[1, 2], [], []]
# check that your code works correctly on provided example
print(reverseGraph(adj_list))
assert reverseGraph(adj_list) == [[], [0], [0]], 'Wrong answer'


def isTransitive(adj_list):
    # Given an adjacency list for the directed
    # graph determine if the relation between
    # objects represented by a graph has the transitive
    # property. (meaning that if there are edges v1 -> v2
    # and v2 -> v3 there exists an edge v1 -> v3)
    n = len(adj_list)
    is_transitive = True
    for index, edges in enumerate(adj_list):
        for edge in edges:
            start_set = set(edges)
            destination_set = set(adj_list[edge])
            if destination_set.difference(start_set) != set():
                is_transitive = False
                break
    return is_transitive

adj_list = [[1, 2], [2], []]
# check that your code works correctly on provided example
print(isTransitive(adj_list))
assert isTransitive(adj_list), 'Wrong answer'


def vertexDegree(vertex_count, edge_list):
    #Given an edge list for an undirected
    # graph count the degree of each vertex.
    # (The degree of a vertex is the number
    # of edges incident to the given vertex)
    n = vertex_count
    degrees = [0 for i in range(n)]
    for edge in edge_list:
        e_from, e_to = edge
        degrees[e_from] += 1
        degrees[e_to] += 1
    return degrees

vertex_count = 3
edge_list = [[0, 1], [0, 2]]
# check that your code works correctly on provided example
print(vertexDegree(vertex_count, edge_list))
assert vertexDegree(vertex_count, edge_list) == [2, 1, 1], 'Wrong answer'


def hasDuplicates(vertex_count, edge_list):
    #Given an edge list for an undirected graph
    # check if the graph has duplicate edges.
    n = vertex_count
    has_duplicates = False
    edge_set = set()
    for edge in edge_list:
        if tuple(edge) not in edge_set or tuple(edge[::-1]) not in edge_set:
            edge_set.update({tuple(edge)})
            edge_set.update({tuple(edge[::-1])})
        else:
            has_duplicates = True
            break
    return has_duplicates


vertex_count = 2
edge_list = [[0, 1], [1, 0]]
# check that your code works correctly on provided example
print("has_duplicates answer:")
print(hasDuplicates(vertex_count, edge_list))
assert hasDuplicates(vertex_count, edge_list), 'Wrong answer'


def isComplete(vertex_count, edge_list):
    # Given an edge list for an undirected graph
    # check if the graph is complete. (The graph
    # is complete if for every pair of vertices there
    # exists an edge connecting them)
    n = vertex_count
    is_complete = True
    degrees = [0 for i in range(n)]
    for edge in edge_list:
        e_from, e_to = edge
        degrees[e_from] += 1
        degrees[e_to] += 1
    is_complete = min(degrees) == max(degrees) == n - 1
    return is_complete


vertex_count = 2
edge_list = [[0, 1]]
# check that your code works correctly on provided example
print("isCompelte answer:")
print(isComplete(vertex_count, edge_list))
assert isComplete(vertex_count, edge_list), 'Wrong answer'
