class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-val for val in freq.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0

        while q or max_heap:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time

        
