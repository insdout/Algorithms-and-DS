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
        if t_hash == p_hash:
            for ind, char in enumerate(text[i:i + n]):
                if char != pattern[ind]:
                    continue
            indices.append(i)
        if i < len(text) - n:
            t_hash = hash_update(p, q, p_power, t_hash, text[i], text[i+n])

    return indices


if __name__ == "__main__":

    text = 'abracadabra'
    pattern = 'ab'
    # check that your code works correctly on provided example
    assert RabinKarp(text, pattern) == [0, 7], 'Wrong answer'