# 1
# Дано шахматное поле и 2 клетки на нём. Найти наименьшее число ходов коня,
# которое требуется, чтобы с первой клетки достичь второй.
# =========================================================================================


from collections import deque
from math import log2
from math import floor
import binarytree


def min_moves_knight(board_size, v_from, v_to):
    adj_list = {}
    for i in range(board_size):
        for j in range(board_size):
            for x in [2, -2]:
                for y in [1, -1]:
                    if 0 <= i + x < board_size and 0 <= j + y < board_size:
                        adj_list.setdefault((i, j), []).append((i + x, j + y))
                    if 0 <= j + x < board_size and 0 <= i + y < board_size:
                        adj_list.setdefault((i, j), []).append((i + y, j + x))
    #print(adj_list)
    return distance(adj_list, v_from, v_to)


def distance(adj_list, v_from, v_to):
    n = len(adj_list)
    distance = -1

    visited = {(i, j): False for i in range(n) for j in range(n)}
    Q = deque()
    Q.append((distance + 1, v_from))
    visited[v_from] = True
    while len(Q) > 0:
        cur_dist, cur_v = Q.popleft()
        if cur_v == v_to:
            distance = cur_dist
        for neighbor in adj_list[cur_v]:
            if not visited[neighbor]:
                Q.append((cur_dist + 1, neighbor))
                visited[neighbor] = True

    return distance


assert min_moves_knight(4, (0, 0), (1, 2)) == 1, "Wrong Answer"
assert min_moves_knight(4, (0, 0), (0, 2)) == 2, "Wrong Answer"
assert min_moves_knight(4, (0, 0), (2, 3)) == 3, "Wrong Answer"


# 2
# Дано дерево и 2 вершины в нем, найти их наименьшего общего предка
# =========================================================================================


class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


def insert(root, node):
    if root.key > node.key:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)


def find_common_ancestor(root, u, v):
    u_ref = None
    v_ref = None
    common_ancestor = False
    parent_dict = {}
    if root is None:
        return common_ancestor
    q = deque()
    q.append(root)
    while len(q) > 0:
        cur_node = q.popleft()
        if cur_node.key == u:
            u_ref = cur_node
        if cur_node.key == v:
            v_ref = cur_node
        if cur_node.left is not None:
            q.append(cur_node.left)
            parent_dict[cur_node.left] = cur_node
        if cur_node.right is not None:
            q.append(cur_node.right)
            parent_dict[cur_node.right] = cur_node

    if u_ref is None or v_ref is None:
        return common_ancestor
    path_u = []
    path_v = []
    while u_ref != root:
        path_u.insert(0, u_ref.key)
        u_ref = parent_dict[u_ref]
    path_u.insert(0, root.key)
    while v_ref != root:
        path_v.insert(0, v_ref.key)
        v_ref = parent_dict[v_ref]
    path_v.insert(0, root.key)
    i = 0
    while path_v[i] == path_u[i]:
        common_ancestor = path_v[i]
        i += 1
    print(path_u)
    print(path_v)
    return common_ancestor


print()
print("Задание 2.")
T = Node(10)
for i in [5, 15, 3, 6, 14, 16, 2, 7, 11, 19, 4]:
    insert(T, Node(i))

print("наименьший общий предок:", find_common_ancestor(T, 7, 11))


def convert_to_bintree(root):
    new_root = binarytree.Node(root.key)
    if root.left != None:
        new_root.left = convert_to_bintree(root.left)
    if root.right != None:
        new_root.right = convert_to_bintree(root.right)
    return new_root


def print_tree(root):
    print(convert_to_bintree(root))

print_tree(T)


# 3.
# Дано дерево. Назовём шириной уровня количество вершин одной глубины, которое располагалось бы между крайними
# вершинами нашего дерева, включая их, при условии, что дерево было бы полным
# Найти максимальную ширину дерева
# =========================================================================================

def max_width(root):
    stack = []
    nodes_count = 0
    if root is None:
        return False
    stack.append(root)
    while len(stack) > 0:
        cur_node = stack.pop()
        nodes_count += 1
        if cur_node.left is not None:
            stack.append(cur_node.left)
        if cur_node.right is not None:
            stack.append(cur_node.right)
    print("Всего вершин:", nodes_count)
    tree_height = floor(log2(nodes_count))
    print("Высота полного дерева на", nodes_count, "вершинах:", tree_height)
    width = max(2**(tree_height-1), nodes_count-2**tree_height+1)
    return width

print()
print("Задание 3.")
print("Макс ширина: ", max_width(T))

# 4.
# Запрограммировать префикс-функцию. С ее помощью проверить вхождение подстроки в строку
# =========================================================================================

def prefix(s):
    n = len(s)
    p = [0 for _ in range(n)]
    p[0] = 0
    for j in range(1, n):
        i = p[j-1]
        while i > 0 and s[i] != s[j]:
            i = p[i-1]
        if s[i] == s[j]:
            p[j] = i + 1
    return p


print()
print("Задание 4. Префикс")
s = "bababacbba"
print("Префикс функция для строки", s, ":", prefix(s))


def substring_match(s, pattern):
    q = pattern + "#" + s
    prefix_array = prefix(q)
    match_indexes = [i - len(pattern) - 1 for i in range(len(q)) if prefix_array[i] == len(pattern)]
    for index in match_indexes:
        start = index - len(pattern) + 1
        end = index + 1
        print("from:", start, "to:", end - 1, "string:", s[start:end])
    return match_indexes

print()
print("Задание 4. Подстрока в строке.")
s = "ertqwertyert"
p = "ert"
print("Вхождение паттерна:", p," в строку:", s, "в индексах:", substring_match(s, p))
