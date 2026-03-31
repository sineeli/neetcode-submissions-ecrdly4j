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
        self.unique_count -= 1
        self._ensure_user_exists(userId)
        # Add to front of deque - O(1)
        self.user_tweets[userId].appendleft((self.unique_count, tweetId))
        
        # Optional: Keep only recent tweets to save memory
        if len(self.user_tweets[userId]) > 100:
            self.user_tweets[userId].pop()
    
    def getNewsFeed(self, userId: int) -> List[int]:
        self._ensure_user_exists(userId)
        
        all_recent_tweets = []
        
        # Get up to 10 most recent from user
        for i, tweet in enumerate(self.user_tweets[userId]):
            if i >= 10: break
            all_recent_tweets.append(tweet)
        
        # Get up to 10 most recent from each followee
        for followee in self.users[userId]:
            if followee in self.user_tweets:
                for i, tweet in enumerate(self.user_tweets[followee]):
                    if i >= 10: break
                    all_recent_tweets.append(tweet)
        
        # Sort and return top 10
        all_recent_tweets.sort(key=lambda x: x[0])
        return [tweet[1] for tweet in all_recent_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self._ensure_user_exists(followerId)
            self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)