# In this problem you will be required to improve our text justification algorithm from the lecture.
#
# In real life typesetting, it is okay to have empty space at the end of the last line of a paragraph.
# The goal of this assignment would be to adapt the code from the lecture to find the minimal penalty
# and produce the formatted text given that there is no penalty for the last line.
#
# Part 1. You have to upload a file containing a function tj_cost(L, W), where L is the line width
# and W is a list of words. It is guaranteed that W is nonempty and the length of every word does
# not exceed L. The function should return the smallest possible penalty for a text with words W
# and the line width L given that there is no penalty for the last line.
#
# Example. For L = 15 and W = ["jars", "jaws", "joke", "jury", "juxtaposition"],
# the answer must be 432.
#
# Part 2. You have to upload a file containing a function tj(L, W), where L is the line width
# and W is a list of words. It is guaranteed that W is nonempty and the length of every word
# does not exceed L. The function should return a text (that is, a single string variable with
# words within a line separated by a single space and the lines separated by "\n") acheiving
# the smallest possible penalty for a text with words W and the line width L given that there
# is no penalty for the last line.
#
# Example. For L = 15 and W = ["jars", "jaws", "joke", "jury", "juxtaposition"], the answer must
# be "jars jaws\njoke jury\njuxtaposition".
#
# For both parts, the length of W in the tests will not exceed 500. The time limit for each
# test will be one second.
#
# Partial credit: a half of the points is given if at least half of the tests has been
# successfully passed. Full credit is given only if all tests have been passes.


import math


def tj_cost(L, W):
    n = len(W)
    tbl = [ math.inf ] * (n + 1)
    tbl[0] = 0
    for i in range(1, n + 1):
        length = -1
        w = []
        for j in range(i - 1, -1, -1):
            w.append(W[j])
            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            else:
                P = (L - length)**3
                if i == n:
                    P=0
            #print("b",i, j, tbl,"f:", tbl[i], "s:",tbl[j] + P,"P:", P,w,"len:",length)
            tbl[i] = min(tbl[i], tbl[j] + P)
            #print("a",i,j, tbl,tbl[i], tbl[j] + P,P,w)
    return tbl[n]


def tj(L, W):
    n = len(W)
    tbl = [ math.inf ] * (n + 1)
    tbl_s = [0] * (n + 1)
    tbl[0] = 0
    for i in range(1, n + 1):
        length = -1
        w = []
        for j in range(i - 1, -1, -1):
            w.append(W[j])
            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            else:
                P = (L - length)**3
                if i == n:
                    P=0
            #print("b",i, j, tbl,"f:", tbl[i], "s:",tbl[j] + P,"P:", P,w,"len:",length)
            if tbl[i] > tbl[j] + P:
                tbl[i] = tbl[j] + P
                tbl_s[i] = j
                #print(tbl_s)
            #print("a",i,j, tbl,tbl[i], tbl[j] + P,P,w)
    str_o = []
    remain = n
    while remain > 0:
        str_o.insert(0," ".join(W[tbl_s[remain]:remain]))
        remain -= remain - tbl_s[remain]

    return '\n'.join(str_o)


if __name__ == "__main__":
    W_example = ["jars", "jaws", "joke", "jury", "juxtaposition"]
    L_example = 15
    # should print 432
    print(tj_cost(L_example, W_example))
    # should print:
    #jars jaws
    #joke jury
    #juxtaposition
    print(repr(tj(L_example, W_example)))
