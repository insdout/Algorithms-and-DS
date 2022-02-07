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
