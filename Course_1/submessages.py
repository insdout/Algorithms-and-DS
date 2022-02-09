# Petr Tort would like to reach out to possible alien civilizations. He wants to
# send a short message (e.g., "Hey there!"). However, he know that some of the
# symbols in the message might get lost because of transmission errors.
# He would like to generate all possible strings that could be received by aliens
# to check whether any of them could sound impolite.
#
# Write a recursive algorithm submessages(s) that generates a set of all possible
# strings that could be obtained from s by removing some symbols.
#
# For example, submessages("aba") should return {"", "a", "b", "aa", "ab", "ba", "aba"}.


def submessages(s):
    if len(s) == 0:
        return {""}
    last = s[-1]
    without_last = s[:-1]
    result = submessages(without_last)
    for m in list(result):
        result.add(m + last)
    return result


if __name__ == "__main__":
# should print {"", "a", "b", "aa", "ab", "ba", "aba"}
# elements of the set can be printed in a different order
    print(submessages("aba"))
