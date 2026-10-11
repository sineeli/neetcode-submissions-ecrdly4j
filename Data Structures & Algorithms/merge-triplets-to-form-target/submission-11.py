class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        new_triplets = []
        for triplet in triplets:
            flag = True
            for idx in range(3):
                if triplet[idx] > target[idx]:
                    flag = False
            if flag:
                new_triplets.append(triplet)
        
        if not new_triplets:
            return False
                    
        ans = True
        for i in range(3):
            curr_max = -1
            for triplet in new_triplets:
                curr_max = max(curr_max, triplet[i])
            
            if curr_max != target[i]:
                return False
        
        return ans