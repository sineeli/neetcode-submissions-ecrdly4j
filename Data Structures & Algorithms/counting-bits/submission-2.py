class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count_bit_one(num):
            count = 0
            while num:
                if num & 1:
                    count += 1
                num >>= 1
            
            return count
        
        ans = []
        for i in range(n + 1):
            ans.append(count_bit_one(i))
        
        return ans