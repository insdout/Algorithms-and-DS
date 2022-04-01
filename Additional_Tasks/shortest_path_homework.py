# Дано шахматное поле и 2 клетки на нём. Найти наименьшее число ходов коня,
# которое требуется, чтобы с первой клетки достичь второй.

from collections import deque


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


# 4.
# Запрограммировать префикс-функцию. С ее помощью проверить вхождение подстроки в строку


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

print(prefix("bababacbba"))


def substring_match(s, pattern):
    q = pattern + "#" + s
    prefix_array = prefix(q)
    match_indexes = [i - len(pattern) - 1 for i in range(len(q)) if prefix_array[i] == len(pattern)]
    for index in match_indexes:
        start = index - len(pattern) + 1
        end = index + 1
        print("from:", start, "to:", end - 1, "string:", s[start:end])
    return match_indexes


s = "ertqwertyert"
p = "ert"
print(substring_match(s, p))
