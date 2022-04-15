def removeKdigits( num: str, k: int) -> str:
    stack = [num[0]]
    if len(num) == 1:
        return "0"
    for i in range(1, len(num)):
        while stack and stack[-1] > num[i] and k:
            stack.pop()
            k -= 1
        stack.append(num[i])
        # print(stack)
    while k and stack:
        stack.pop()
        k -= 1
    ans = "".join(stack) if stack else "0"
    return str(int(ans))

input = "10200"
print(removeKdigits(input, 2))