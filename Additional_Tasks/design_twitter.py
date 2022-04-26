# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
# and is able to see the 10 most recent tweets in the user's news feed.
#
# Implement the Twitter class:
#
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
# Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
# Each item in the news feed must be posted by users who the user followed or by the user themself.
# Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId)
# The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId)
# The user with ID followerId started unfollowing the user with ID followeeId.


# Runtime: 64 ms
# Memory Usage: 14 MB

class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        authors = self.users.get(userId, set())
        authors.add(userId)
        last = len(self.tweets) - 1
        in_feed = 10
        while in_feed and last >= 0:
            if self.tweets[last][0] in authors:
                feed.append(self.tweets[last][1])
                in_feed -= 1
            last -= 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            if followeeId in self.users[followerId]:
                self.users[followerId].remove(followeeId)



# Runtime: 52 ms
# Memory Usage: 14.1 MB

import heapq

class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((self.tweet_count, tweetId))
        self.tweet_count -= 1
        #print(self.tweets)

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        res = []
        authors = self.users.get(userId, set())
        authors.add(userId)
        for author in authors:
            last_index = len(self.tweets.get(author, [])) - 1
            if last_index >= 0:
                tweet_count, tweet_id = self.tweets[author][last_index]
                heap.append((tweet_count, tweet_id, author, last_index))
        heapq.heapify(heap)
        while heap and len(res) <= 10:
            tweet_count, tweet_id, author, last_index = heapq.heappop(heap)
            res.append(tweet_id)
            if last_index >= 0:
                tweet_count, tweet_id = self.tweets[author][last_index - 1]
                heap.append((tweet_count, tweet_id, author, last_index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            if followeeId in self.users[followerId]:
                self.users[followerId].remove(followeeId)

if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5) # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 6)  # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 7)  # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 8)  # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 9)  # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 10)  # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 11)  # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 12)  # User 1 posts a new tweet (id = 5).
    print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2)    # User 1 follows user 2.
    twitter.postTweet(2, 33) # User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 34)  # User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 35)  # User 2 posts a new tweet (id = 6).
    print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2)  # User 1 unfollows user 2.
    print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.