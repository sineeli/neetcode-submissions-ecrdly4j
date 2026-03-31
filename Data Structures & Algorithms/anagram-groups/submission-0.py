class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for string in strs:
            output["".join(sorted(string))].append(string)
        
        return output.values()


        