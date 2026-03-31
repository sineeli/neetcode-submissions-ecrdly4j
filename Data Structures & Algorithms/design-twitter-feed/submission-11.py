class Twitter:
    def __init__(self):
        self.users = {}
        self.user_tweets = {}
        self.unique_count = 0
    
    def _ensure_user_exists(self, userId: int):
        if userId not in self.users:
            self.users[userId] = set()
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.unique_count -= 1
        self._ensure_user_exists(userId)
        self.user_tweets[userId].append((self.unique_count, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self._ensure_user_exists(userId)
        
        total_tweets = self.user_tweets[userId].copy()
        for followee in self.users[userId]:
            if followee in self.user_tweets:
                total_tweets.extend(self.user_tweets[followee])
        
        heapq.heapify(total_tweets)
        latest = []
        for _ in range(min(10, len(total_tweets))):
            tweet = heapq.heappop(total_tweets)
            latest.append(tweet[1])
        return latest

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self._ensure_user_exists(followerId)
            self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)