# Consider the following function that generates all the subsets of a list of given size kk

def subsets(elems, k):
    if k == 0:
        return [ [] ]
    if len(elems) == 0:
        return []
    last = elems[-1]
    without_last = elems[:-1]
    result = subsets(without_last, k)
    with_last = subsets(without_last, k - 1)
    for s in with_last:
        result.append(s + [last])
    return result


if __name__ == "__main__":
    S = subsets(list(range(100)), 4)
    print(S[4])