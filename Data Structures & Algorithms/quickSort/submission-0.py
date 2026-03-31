# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) - 1
        self.quick_sort(pairs, s, e)
        return pairs
    
    def quick_sort(self, pairs, s, e):
        if e - s + 1 <= 1:
            return
        
        pivot = pairs[e]
        left = s

        for i in range(s, e+1):
            if pairs[i].key < pivot.key:
                tmp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = tmp
                left += 1
        
        pairs[e] = pairs[left]
        pairs[left] = pivot
        self.quick_sort(pairs, s, left-1)
        self.quick_sort(pairs, left+1, e)
        