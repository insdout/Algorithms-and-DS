# Given an array of strings words and an integer k, return the k most frequent strings.
#
# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency
# by their lexicographical order.
#
# Example 1:
#
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

# Runtime: 73 ms, faster than 60.71% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 13.9 MB, less than 68.45% of Python3 online submissions for Top K Frequent Words.

def topKFrequent(words: list[str], k: int) -> list[str]:
    d = {}
    for word in words:
        d[word] = d.get(word, 0) + 1
    ans = sorted(d.keys(), key=lambda x: (-d[x], x), reverse=False)
    return ans[:k]


if __name__ == "__main__":
    print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
    print(topKFrequent(
        ["zthe", "zthe", "zthe", "zthe", "bthe","day","is","sunny","bthe","bthe","bthe","sunny","is","is"],
        k = 4))