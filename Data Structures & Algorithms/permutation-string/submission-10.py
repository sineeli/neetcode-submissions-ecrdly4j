class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        main_s1_count = Counter(s1)
        temp_dict = {}
        l = 0
        for r in range(0, n):
            temp_dict[s2[r]] = temp_dict.get(s2[r], 0) + 1
            if r - l + 1 > m:
                temp_dict[s2[l]] -= 1
                if temp_dict[s2[l]] == 0:
                    del temp_dict[s2[l]]
                l += 1
            if (r - l + 1) == m and temp_dict == main_s1_count:
                return True

        return False

        