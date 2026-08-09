class Twitter:
    def __init__(self):
        self.users = {}
        self.user_tweets = {}
        self.unique_count = 0

    def _ensure_user_exists(self, userId: int):
        if userId not in self.users:
            self.users[userId] = set()
        if userId not in self.user_tweets:
            self.user_tweets[userId] = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._ensure_user_exists(userId)
        self.user_tweets[userId].appendleft((self.unique_count, tweetId))
        self.unique_count += 1

        if len(self.user_tweets[userId]) > 10:
            self.user_tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        self._ensure_user_exists(userId)

        all_recent_tweets = []

        for i, tweet in enumerate(self.user_tweets[userId]):
            if i >= 10:
                break
            all_recent_tweets.append(tweet)

        for followee in self.users[userId]:
            if followee in self.user_tweets:
                for i, tweet in enumerate(self.user_tweets[followee]):
                    if i >= 10:
                        break
                    all_recent_tweets.append(tweet)

        all_recent_tweets.sort(key=lambda x: x[0], reverse=True)
        return [tweet[1] for tweet in all_recent_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self._ensure_user_exists(followerId)
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
