# I type "algotrhms and bata ctuctres" in google and it suggests to show me results about
# "algorithms and data structures". Somehow it understands that these two strings are similar,
# and I have just made several typos.
# Understanding similarity between two strings or texts is crucial for many applications
# such as search for plagiarism, version control, and genetics. Unlike the example with the search query,
# these applications require to measure the similarity between pretty long strings.
# The goal of this assignment is to develop such an algorithm.
# The formal problem is the following
#
# Input: strings A and B
# Output: the smallest number of operations (insertion, deletion, and substitution) needed to transform A to B.
# This number is usually called the edit distance. For example, the edit distance between "good"
# and "bad" is three: good -> ood -> bod -> bad.
# We will approach this problem using dynamic programming. Let |A| = n and |B| = m.
# We will fill a (n + 1) \times (m + 1)(n+1)×(m+1) table DD such that D[i][j] will be the
# edit distance between A[:i]A[:i] and B[:j]B[:j]. We will derive a recurrence
# to compute D[i][j]D[i][j]. Consider two cases:
#
# Case A[i - 1] = B[j - 1] Then we can focus on beginnigns of both strings,
# so D[i][j]=D[i−1][j−1].
#
# Case A[i - 1] != B[j - 1]
# Since we want ultimately make the stings equal, there are three options
#
# We delete A[i−1]. The remaining number of operations is D[i−1][j]
# We delete B[j−1]. The remaining number of operations is D[i][j−1]
# We substitute A[i−1] for B[j−1]. The remaining number of operations is D[i−1][j−1].
#
# Therefore, in this case D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
#
# Part 1.  Write a function edistance(A, B) using the above recurrence.
#
# Part 2. Write a function weighted_edistance(A, B, wdel, wins, wsub) that computes
# the minimal total weight of the operations to make A from B if wdel, wins, wsub
# are positive integer weights of deletion, insertion, and substitution, respectively.
#
# For example, if wdel = wins = 1 and wsub = 3, the weighted distance between good
# and bad becomes 5: good -> ood -> od -> d -> ad -> bad.
#
# Part 3. Write a function edistance_substring(A, B) that returns the smallest edit
# distance between a substring of A (that is, a string of the from A[i:j]) and B.
# In other words, it is allowed to delete some symbols at the beginning and at the end of A for free.
#
# For example, if A = good and B = bad, then the output should be 2,
# because one can transform ood into bad with two subtitutions, and at least two operations
# are necessary because the letters b and a are not present in A.
# The complexity of all these functions should be O(|A| |B|),
# so |A| = |B| = 200 ∣A∣=∣B∣=200 should be fast.
#
# Here is a file with function definitions and a couple of sample input-output pairs:

import math


def edistance(A, B):
    n = len(A)
    m = len(B)
    D = [[math.inf for _ in range(m+1)] for _ in range(n+1)]
    for i in range(0, n + 1):
        for j in range(0, m+1):
            if i == 0:
                D[i][j] = j
            elif j == 0:
                D[i][j] = i
            elif A[i-1]==B[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = 1 + min(D[i-1][j],D[i][j-1],D[i-1][j-1])

    return D[n][m]


def weighted_edistance(A, B, wdel, wins, wsub):
    n = len(A)
    m = len(B)
    D = [[math.inf for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if i == 0:
                D[i][j] = j*wins
            elif j == 0:
                D[i][j] = i*wdel
            elif A[i - 1] == B[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = min(
                    wdel + D[i - 1][j],
                    wins + D[i][j - 1],
                    wsub + D[i - 1][j - 1]
                )

    return D[n][m]


# edistance_substring should be corrected. Have three versions 2 give wrong results. Why?

def edistance_substring(B, A):
    n = len(A)
    m = len(B)
    D = [[math.inf for _ in range(m+1)] for _ in range(n+1)]
    for i in range(0, n + 1):
        for j in range(0, m+1):
            if i == 0:
                D[i][j] = 0
            elif j == 0:
                D[i][j] = i
            elif A[i-1]==B[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = 1 + min(D[i-1][j],D[i][j-1],D[i-1][j-1])
    #print(D)
    return min(D[-1])


def edistance_substring2(A, B):
    n = len(A)
    m = len(B)
    D = [[math.inf for _ in range(m+1)] for _ in range(n+1)]
    for i in range(0, n + 1):
        for j in range(0, m+1):
            if i == 0:
                D[i][j] = j
            elif j == 0:
                D[i][j] = 0
            elif A[i-1] == B[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = 1 + min(D[i-1][j], D[i][j-1], D[i-1][j-1])

    return D[-1][-1]


def edistance_substring3(A, B):
    n = len(A)
    m = len(B)
    tbl = [[math.inf] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        tbl[i][0] = 0
    for j in range(m + 1):
        tbl[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                tbl[i][j] = tbl[i - 1][j - 1]
            elif A[i - 1] != B[j - 1]:
                tbl[i][j] = 1 + min(tbl[i - 1][j], tbl[i][j - 1], tbl[i - 1][j - 1])
    return tbl[-1][-1]

if __name__ == "__main__":
    # should print 1
    print(edistance("b", "bb"))
    # should print 3
    print(edistance("good", "bad"))
    # should print 1
    print(edistance("g", "b"))
    # should print 1
    print(edistance("b", "bb"))
    # should print 7
    print(weighted_edistance("good", "bad", 1, 2, 5))
    # should print 0
    print(edistance_substring("good", "bad"))

    print("compare 3 versions of edistance_substring:")
    a = "sabas"
    b = "aba"
    print("from:", a, "to:", b, "in:", edistance_substring(a, b))
    print("from:", a, "to:", b, "in:", edistance_substring2(a, b))
    print("from:", a, "to:", b, "in:", edistance_substring3(a, b))
