class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_map = {}

        for h in hand:
            hand_map[h] = hand_map.get(h, 0) + 1

        minH = list(hand_map.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in hand_map:
                    return False
                hand_map[i] -= 1
                if hand_map[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True
