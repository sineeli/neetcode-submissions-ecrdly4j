class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        res = []
        print(n)
        while i < n:
            temp = []
            while i < n and s[i] != "#":
                temp.append(s[i])
                i += 1
            i += 1 # for hash
            temp_output = []
            curr_i = i
            while i < curr_i + int("".join(temp)):
                temp_output.append(s[i])
                i += 1
            res.append("".join(temp_output))
        
        return res

            

