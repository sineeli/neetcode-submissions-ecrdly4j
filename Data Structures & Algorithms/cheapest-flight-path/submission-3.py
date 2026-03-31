class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        for stops in range(k + 1):
            temp = dist[:]
            print(f"Before: {temp} Stops {stops}")
            for from_city, to_city, price in flights:
                if dist[from_city] != INF:
                    print(f"from: {from_city}, to: {to_city}, price: {price}" )
                    if price + dist[from_city] < temp[to_city]:
                        temp[to_city] = price + dist[from_city]
                    print(f"Travelling Cost: {min(temp[to_city], price + temp[from_city])}")
                
            print(f"After: {temp} Stops {stops}")
            dist = temp
        
        return dist[dst] if dist[dst] != INF else -1

        