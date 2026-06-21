class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)
        for ana in strs:
            s = [0] * 26
            for c in ana:
                s[ord(c) - 97] += 1
            res_dict[tuple(s)].append(ana)
        
        return list(res_dict.values())