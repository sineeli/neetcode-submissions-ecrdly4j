class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count_bits(num):
            count = 0
            while num > 0:
                count += num & 1
                num = num >> 1
                # print(num)
            return count
        total = []
        for i in range(n+1):
            total.append(count_bits(i))

        return total