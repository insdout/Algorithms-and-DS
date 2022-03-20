# Given the adjacency list of an undirected graph check if a graph is a tree.

graph = []
visited = []


# USE DFS

def dfs(v, e_from):
    global graph, visited
    visited[v] = True
    is_tree = True
    path = [v]
    print("dfs start:")
    print("at", v, "from", e_from)
    print("====================")
    for u in graph[v]:
        if not visited[u]:
            r_is_tree, r_path = dfs(u, v)
            is_tree = is_tree and r_is_tree
            print("recursive call:")
            print("from", v, "to", u)
            print("visited", visited)
            print("v", v,"u", u,"path", path, "r_path", r_path)
            path.extend(r_path)
            print("after", path)
            print("====================")
        elif visited[u] and u != e_from:
            is_tree = False
            return is_tree, path
    return is_tree, path



def isTree(adj_list):
    global graph, visited
    n = len(adj_list)

    graph = adj_list
    visited = [False for i in range(n)]

    is_tree = True

    is_tree, vertexes = dfs(0, 0)
    if len(set(vertexes)) == n:
        return is_tree
    else:
        return False


adj_list = [[1, 2], [0], [0]]
# check that your code works correctly on provided example
print("Ans:", isTree(adj_list))
assert isTree(adj_list), 'Wrong answer'

print()
print("Second case:")
adj_list = [[1, 2], [0], [0, 3, 4], [2, 5], [2, 5], [3, 4]]
# check that your code works correctly on provided example
print("Ans:", isTree(adj_list))