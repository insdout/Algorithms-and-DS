# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

def candy(ratings: list[int]) -> int:
    candies = [1 for _ in range(len(ratings))]
    for i in range(1, len(candies)):
        if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
            candies[i] = candies[i-1] + 1

    for i in reversed(range(1, len(candies))):
        if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
            candies[i-1] = candies[i] + 1
    return sum(candies)


if __name__ == "__main__":
    assert candy([1, 0, 2]) == 5, "Wrong Answer"
    assert candy([1, 2, 2]) == 4, "Wrong Answer"