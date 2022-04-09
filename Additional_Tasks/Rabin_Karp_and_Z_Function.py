def RabinKarp(text, pattern):
    p, q = 31, 10 ** 9 + 7
    indices = []
    p_power = [1]
    n = len(pattern)

    def ord_c(c):
        return ord(c) - ord("a") + 1

    for i in range(1, n):
        p_power.append(p_power[i - 1] * p)

    def hash_f(q, p_power, s):
        res = 0
        for i in range(len(s)):
            res += ord_c(s[i]) * p_power[i]
        return res % q

    def hash_update(p, q, p_power, old_hash, old_char, new_char):
        new_hash = ((old_hash - ord_c(old_char))//p + ord_c(new_char)*p_power[n-1]) % q
        return new_hash

    p_hash = hash_f(q, p_power, pattern)
    t_hash = hash_f(q, p_power, text[0:n])
    for i in range(len(text) - n+1):
        print("hash_comp", hash_f(q, p_power, text[i:i+n]))
        if t_hash == p_hash:
            for ind, char in enumerate(text[i:i + n]):
                if char != pattern[ind]:
                    continue
            indices.append(i)
        if i < len(text) - n:
            t_hash = hash_update(p, q, p_power, t_hash, text[i], text[i+n])
            print(text[i], text[i+n], text[i:i+n], t_hash)

    print(indices)
    return indices


def zAlgorithm(text, pattern):
    n, m = len(text), len(pattern)
    special_symbol = "#"
    indices = []
    joined_string = pattern + special_symbol + text

    def zFunction(text):
        n = len(text)
        z_func = [0 for i in range(n)]
        l, r, k = 0, 0, 0
        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and text[r - l] == text[r]:
                    r += 1
                z_func[i] = r - l
                r -= 1
            else:
                k = i - l
                if z_func[k] < r - i + 1:
                    z_func[i] = z_func[k]
                else:
                    l = i
                    while r < n and text[r - l] == text[r]:
                        r += 1
                    z_func[i] = r - l
                    r -= 1
        return z_func

    for ind, value in enumerate(zFunction(joined_string)):
        if value == m:
            indices.append(ind - m - 1)

    return indices


if __name__ == "__main__":
    text = 'abracadabra'
    pattern = 'ab'
    # check that your code works correctly on provided example
    assert zAlgorithm(text, pattern) == [0, 7], 'Wrong answer'

    text = 'abracadabra'
    pattern = 'ab'
    # check that your code works correctly on provided example
    assert RabinKarp(text, pattern) == [0, 7], 'Wrong answer'