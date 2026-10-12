class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_dict = {}

        for idx, c in enumerate(s):
            idx_dict[c] = idx
        
        print(idx_dict)
        
        curr_seen = set()
        output = []
        size = end = 0
        for idx, c in enumerate(s):
            size += 1
            end = max(end, idx_dict[c])
            
            if idx == end:
                output.append(size)
                size = 0
        
        return output
            
