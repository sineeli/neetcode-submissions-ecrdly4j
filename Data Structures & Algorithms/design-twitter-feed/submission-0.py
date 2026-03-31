class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.graph = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append([self.count, tweetId])
        self.count -= 1
            

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []   
        self.graph[userId].add(userId)
        for followeeId in self.graph[userId]:
            if followeeId in self.users:
                index = len(self.users[followeeId]) - 1
                count, tweetId = self.users[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.users[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.graph[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.graph[followerId]:
            self.graph[followerId].remove(followeeId)

        
