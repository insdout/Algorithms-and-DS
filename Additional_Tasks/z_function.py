
def z_function(s: str):
    n = len(s)
    z = [0 for _ in range(n)]
    left, right = 0, 0
    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while z[i] + i < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if z[i] + i - 1 > right:
            left = i
            right = z[i] + i - 1
    return z


def z_algorithm(string, pattern):
    z = z_function(pattern + "#" + string)
    indices = [i - len(pattern) - 1 for i in range(len(z)) if z[i] == len(pattern)]
    return indices


if __name__ == "__main__":
    text = 'abracadabra'
    pattern = 'ab'
    # check that your code works correctly on provided example
    print(z_algorithm(text, pattern))
    assert z_algorithm(text, pattern) == [0, 7], 'Wrong answer'

    text = 'abracadabra'
    pattern = 'abc'
    # check that your code works correctly on provided example
    print(z_algorithm(text, pattern))
    assert z_algorithm(text, pattern) == [], 'Wrong answer'

    text = 'abracadabra'
    pattern = 'ab'
    # check that your code works correctly on provided example
    #assert RabinKarp(text, pattern) == [0, 7], 'Wrong answer'
