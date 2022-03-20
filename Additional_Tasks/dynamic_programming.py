# ======================  1  =============================
# Найти максимальную сумму элементов подмассивов в массиве.
# ========================================================

import math


def max_subarray(a):
    b = []
    if len(a) == 0:
        return -math.inf
    b.append(a[0])
    if len(a) == 1:
        return b[0]
    for i in range(1, len(a)):
        b.append(max(a[i], b[i-1] + a[i]))
    return max(b)


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
    a = [0]*(n+1)
    a[0] = 1
    a[1] = 1
    if n == 1:
        return a[1]
    for i in range(2, n+1):
        for j in range(i):
            a[i] += a[j]*a[i-j-1]
    return a[n]


print("Answer 4")
print(bst_count(1))
print(bst_count(2))
print(bst_count(3))
print(bst_count(4))
print(bst_count(5))
print(bst_count(6))


# ======================  5  =============================
#  Найти самый длинный палиндром в строке латинских букв
# ========================================================

def largest_palindrome(s):
    max_len = 1
    start = 0
    for i in range(1, len(s)):
        left = i - 1
        right = i
        while left > 0 and right < len(s)-1 and s[left] == s[right]:
            if s[left-1] == s[right+1]:
                left -= 1
                right += 1
            else:
                break
        if right - left + 1 > max_len:
            start = left
            max_len = right - left + 1

        left = i - 1
        right = i + 1
        while left > 0 and right < len(s)-1 and s[left] == s[right]:
            if s[left-1] == s[right+1]:
                left -= 1
                right += 1
            else:
                break
        if right - left + 1 > max_len:
            start = left
            max_len = right - left + 1
    return s[start: start+max_len]

s = "qwerty"
print(largest_palindrome(s))
s = "qweeeersrty"
print(largest_palindrome(s))
s = "qweeeetrsrty"
print(largest_palindrome(s))
s = "qwrsrtyeeee"
print(largest_palindrome(s))
s = "qweebbeetrsrt"
print(largest_palindrome(s))


# ======================  6  =============================
#  Дан массив ячеек, заполненный натуральными числами,
#  каждое число - максимальная длина прыжка с этой ячейки.
#  Необходимо найти минимальное количество прыжков,
#  которые потребуются для достижения последней ячейки
# ========================================================

def jumps(a):
    b = [0]*len(a)
    for i in range(1, len(a)):
        b[i] = math.inf
        for j in range(i):
            if j + a[j] >= i and b[j] != math.inf:
                b[i] = min(b[i], b[j] + 1)
    return b

def jumps2(a):
    b = [0]*len(a)
    temp = a[0]
    temp_index = 0
    b[0] = 0
    for i in range(1, len(a)):
        temp -= 1
        if temp >= 0:
            b[i] = b[temp_index] + 1
        else:
            b[i] = b[i-1] + 1
        if temp < a[i]:
            temp = a[i]
            temp_index = i
    return b[-1]

a = [1, 3, 6, 1, 0, 9]
print("Answer 6")
print(jumps(a))
a = [1, 9, 6, 1, 0, 9]
print(jumps2(a))
