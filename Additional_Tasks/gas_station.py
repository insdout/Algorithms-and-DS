def canCompleteCircuit(gas, cost) -> int:
    if sum(cost) > sum(gas):
        return -1
    diff = [g - c for g, c in zip(gas, cost)]
    diff_acc = [diff[0]]
    for i in range(1, len(diff)):
        diff_acc.append(diff_acc[-1] + diff[i])
    print(diff, diff_acc)
    ind = diff_acc.index(min(diff_acc)) + 1

    if max(diff_acc) < 0:
        return -1
    else:
        return ind % len(gas)
    print(ind)

if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(canCompleteCircuit(gas, cost))