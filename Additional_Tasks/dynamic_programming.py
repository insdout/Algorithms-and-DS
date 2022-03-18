# ======================  1  =============================
# Найти максимальную сумму элементов подмассивов в массиве.
# ========================================================

import math


def max_subarray(a):
    b = []
    if len(a) == 0:
        return -math.inf
    b.append(max(a[0], 0))
    if len(a) == 1:
        return b[0]
    for i in range(1, len(a)):
        b.append(max(a[i], b[i-1] + a[i]))
    return b[-1]


a = [-1, 1, 1, 1, -10, 1, 1, 1, 1]
# Should print 4
print("Answer Task 1:")
print(max_subarray(a))


# ======================  2  =============================
#  Дана бинарная матрица, где 0 означает препятствие,
#  а 1 - возможность прохода.
#  Найти количество путей из верхнего левого угла в нижний правый.
# ========================================================

def maze(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*n for _ in range(m)]
    b[0][0] = 1
    for i in range(1, m):
        if a[0][i] == 1:
            b[0][i] = b[0][i-1]
        else:
            b[0][i] = 0
    for i in range(1, n):
        if a[i][0] == 1:
            b[i][0] = b[i-1][0]
        else:
            b[i][0] = 0
    for i in range(1, n):
        for j in range(1, m):
            if a[i][j] == 1:
                b[i][j] = b[i-1][j] + b[i][j-1]
            else:
                b[i][j] = 0
    return b


print()
print("Answer Task 2:")
a = [[1, 1, 0],
     [1, 1, 0],
     [1, 1, 1]]
print(*maze(a), sep="\n")
print(maze(a)[-1][-1])


# ======================  3  =============================
#  Почитать про Ханойские башни (описание задачи, но не идею решения).
#  Запрогать функцию нахождения минимального количества перемещений
#  в зависимости от числа колец n
# ========================================================

def hanoi_tower_moves(n, source, destination, temp):
    if n >= 1:
        hanoi_tower_moves(n-1, source, temp, destination)
        print(f"move {n} from {source} -> {destination}")
        hanoi_tower_moves(n - 1, temp, destination, source)


hanoi_tower_moves(3, 1, 3, 2)


def hanoi_tomer_min_steps(n):
    # Минимальное количество шагов для башни из n колец.
    # Base Case: n=1 -> 1 шаг
    # Шаг a[n] = 2*a[n-1] + 1
    a = []
    if n <= 0:
        return -math.inf
    a.append(1)
    for i in range(1, n):
        a.append(2*a[-1]+1)
    return a[-1]


print(hanoi_tomer_min_steps(3))


# ======================  4  =============================
#  Найти количество различных BST, содержащих числа от 1 до n
# ========================================================

def bst_count(n):
    return
